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
            var factions = {
                'CY': 'Cygnar',
                'ME': 'The Protectorate of Menoth',
                'KD': 'Khador',
                'CX': 'Cryx',
                'RT': 'Retribution of Scyrah',
                'CV': 'Convergence of Cyriss',
                'MC': 'Mercenaries',
                'TR': 'Trollbloods',
                'CO': 'Circle Orboros',
                'SK': 'Skorne',
                'LG': 'Legion of Everblight',
                'MN': 'Minions'
            };
            var points = [15, 25, 35, 50];
            var that = this;
            var id = options.id;
            if(options.id) {
                var army = new ArmyModel({id: id});
                var entries = new ListEntryCollection();
                var data = $.param({list: id});
                that.army = army;
                $.when(entries.fetch({
                    data: data
                })).done( function() {
                    army.fetch({
                        success: function(army){
                            var template = _.template(armyEditTemplate)({
                                army: army, 
                                entries: entries, 
                                factions: factions, 
                                points: points
                            });
                            that.$el.html(template);
                        }
                    });
                });
            } else {
                var template = _.template(armyEditTemplate)({
                    army: null, 
                    entries: null, 
                    factions: factions,
                    points: points
                });
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
