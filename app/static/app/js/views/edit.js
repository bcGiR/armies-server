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
            var warcasters = new ListEntryCollection();
            var warcasters_data = $.param({
                list: id,
                type: 'WC'
            });
            var units = new ListEntryCollection();
            var units_data = $.param({
                list: id,
                type: 'UN'
            });
            var solos = new ListEntryCollection();
            var solos_data = $.param({
                list: id,
                type: 'SL'
            });
            var attachments = new ListEntryCollection();
            var attachments_data = $.param({
                list: id,
                attached: 'true'
            });
            entries = {
                warcasters: warcasters,
                units: units,
                solos: solos
            };
            that.army = army;
            $.when(warcasters.fetch({
                        data: warcasters_data
                    }),
                    units.fetch({
                        data: units_data
                    }),
                    solos.fetch({
                        data: solos_data
                    }),
                    attachments.fetch({
                        data: attachments_data
                    })
            ).done( function() {
                army.fetch({
                    success: function(army){
                        var faction = FactionCode.getFaction(army.get('faction'));
                        var template = _.template(armyEditTemplate)({
                            army: army, 
                            faction: faction,
                            entries: entries,
                            attachments: attachments
                        });
                        that.$el.html(template);
                    }
                });
            });
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
