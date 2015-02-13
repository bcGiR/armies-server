define([
    'jquery',
    'underscore',
    'backbone',
    'models/army',
    'models/unit',
    'collections/listentries',
    'collections/units',
    'util/serializeobject',
    'text!templates/edit.html'
], function($, _, Backbone, ArmyModel, UnitModel, ListEntryCollection, UnitCollection, serializeObject, armyEditTemplate){
    var EditView = Backbone.View.extend({
        el: '.page',
        render: function(options){
            var that = this;
            var id = options.id;
            if(options.id) {
                var army = new ArmyModel({id: id});
                var units = new UnitCollection();
                var entries = new ListEntryCollection();
                var data = $.param({list: id});
                that.army = army;
                $.when(entries.fetch({
                    data: data,
                    success: function(entries){
                        entries.each(function(entry) {
                            var unit = new UnitModel({id: entry.get('unitpk')});
                            unit.fetch({
                                success: function(unit) {
                                    units.push(unit);
                                }
                            });
                        });
                    }
                })).done( function() {
                    army.fetch({
                        success: function(army){
                            // alert(units.length); ** Gives strange results **
                            var template = _.template(armyEditTemplate)({army: army, units: units});
                            that.$el.html(template);
                        }
                    });
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
