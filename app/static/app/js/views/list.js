define([
    'jquery',
    'underscore',
    'backbone',
    'collections/armies',
    'util/factioncode',
    'text!templates/list.html'
], function($, _, Backbone, ArmyCollection, FactionCode, listTemplate){
    var ListView = Backbone.View.extend({
        el: '.page',
        render: function(options){
            var that = this;
            var faction_code = options.faction_code;
            var points = options.points;
            if (points) {
                var data = $.param({faction: faction_code, points: points});
            } else {
                var data = $.param({faction: faction_code});
            }
            var faction = FactionCode.getFaction(faction_code);
            var armies = new ArmyCollection();
            armies.fetch({
                data: data,
                success: function(armies){
                    var template = _.template(listTemplate)({armies: armies.models,
                                                             faction_code: faction_code,
                                                             faction: faction,
                                                             points: points});
                    that.$el.html(template);
                 }
            });
        }
    });
    return ListView;
});
