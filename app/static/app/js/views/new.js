define([
    'jquery',
    'underscore',
    'backbone',
    'models/army',
    'models/unit',
    'collections/listentries',
    'collections/units',
    'util/serializeobject',
    'text!templates/new.html'
], function($, _, Backbone, ArmyModel, UnitModel, ListEntryCollection, UnitCollection, serializeObject, armyNewTemplate){
    var NewView = Backbone.View.extend({
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
            var template = _.template(armyNewTemplate)({
                    factions: factions,
                    points: points
            });
            this.$el.html(template);
        },
        events: {
            'submit .edit-army-form': 'saveArmy'
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
        }
    });
    return NewView;
});
