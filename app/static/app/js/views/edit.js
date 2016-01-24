define([
    'jquery',
    'underscore',
    'backbone',
    'models/army',
    'models/unit',
    'collections/listentries',
    'collections/units',
    'util/serializeobject',
    'util/factioncode',
    'text!templates/edit.html'
], function($, _, Backbone, ArmyModel, UnitModel, ListEntryCollection, UnitCollection, serializeObject, FactionCode, armyEditTemplate){
    var EditView = Backbone.View.extend({
        el: '.page',
        render: function(options){
            var that = this;
            var id = options.id;
            var army = new ArmyModel({id: id});
            var entries = new ListEntryCollection();
            var entries_data = $.param({
                list: id
            });
            that.army = army;
            console.log(army);
            $.when(entries.fetch({
                        data: entries_data
                    })
            ).done( function() {
                army.fetch({
                    success: function(army){
                        var faction = FactionCode.getFaction(army.get('faction'));
                        var template = _.template(armyEditTemplate)({
                            army: army, 
                            faction: faction,
                            entries: entries
                        });
                        that.$el.html(template);
                    }
                });
            });
        },
        events: {
            'click .update': 'saveArmy',
            'click .delete': 'deleteArmy',
            'click .remove': 'removeUnit'
        },
        saveArmy: function(ev){
            var that = this;
            var army = that.army;
            var armyDetails = army.toJSON();
            army.save(armyDetails, {
                success: function(army){
                    that.goTo('#/list/' + armyDetails.faction);
                }
            });
            return false;
        },
        deleteArmy: function(ev){
            var that = this;
            that.army.destroy({
                success: function(){
                    that.goTo('');
                }
            });
            return false;
        }
    });
    return EditView;
});
