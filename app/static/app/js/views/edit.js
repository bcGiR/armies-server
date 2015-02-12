define([
    'jquery',
    'underscore',
    'backbone',
    'models/army',
    'util/serializeobject',
    'text!templates/edit.html'
], function($, _, Backbone, ArmyModel, serializeObject, armyEditTemplate){
    var EditView = Backbone.View.extend({
        el: '.page',
        render: function(options){
            var that = this;
            if(options.id) {
                var army = new ArmyModel({id: options.id});
                that.army = army;
                army.fetch({
                    success: function(army){
                        var template = _.template(armyEditTemplate)({army: army});
                        that.$el.html(template);
                    }
                });
            } else {
                var template = _.template(armyEditTemplate)({army: null});
                this.$el.html(template);
            }
        },
        events: {
            'submit .edit-army-form': 'saveArmy',
            'click .delete': 'deleteArmy'
        },
        saveArmy: function(ev){
            var armyDetails = $(ev.currentTarget).serializeObject();
            var army = new ArmyModel();
            var that = this;
            army.save(armyDetails, {
                success: function(army){
                    that.undelegateEvents();
                    that.goTo('#/list/' + armyDetails.faction);
                }
            });
            return false;
        },
        deleteArmy: function(ev){
            var that = this;
            this.army.destroy({
                success: function(){
                    that.undelegateEvents();
                    that.goTo('');
                }
            });
            return false;
        }
    });
    return EditView;
});
