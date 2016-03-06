define([
    'jquery',
    'underscore',
    'backbone',
    'models/army',
    'models/unit',
    'collections/listentries',
    'collections/units',
    'util/factioncode',
    'util/getfactionimagepath',
    'text!templates/create.html'
], function($, _, Backbone, ArmyModel, UnitModel, ListEntryCollection, UnitCollection, FactionCode, GetFactionImagePath, createTemplate){
    var CreateViewController = Backbone.View.extend({
        tagName: 'div',
        render: function(options){
            var that = this;
            var army = new ArmyModel({id: id});
            that.army = army;
            var entries = new ListEntryCollection();
            army.fetch({
                success: function(army){
                    var faction = FactionCode.getFaction(army.get("faction"));
                    var factionimagepath = GetFactionImagePath.getImagePath(faction);
                    var template = _.template(createTemplate)({
                        army: army,
                        faction: faction,
                        factionimagepath: factionimagepath,
                        entries: entries
                    });
                    that.$el.html(template);
                }
            });
        },
        events: {
            'click .create': 'saveArmy',
            'click .remove': 'removeUnit'
        },
        saveArmy: function(ev){
            var that = this;
            var army = that.army


});
