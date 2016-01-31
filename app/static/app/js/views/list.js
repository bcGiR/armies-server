define([
    'jquery',
    'underscore',
    'backbone',
    'collections/armies',
    'views/armylistview',
    'util/factioncode',
    'text!templates/list.html'
], function($, _, Backbone, ArmyCollection, ArmyListView, FactionCode, listTemplate){
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
                    var template = _.template(listTemplate)({faction_code: faction_code,
                                                             faction: faction,
                                                             points: points});
                    that.$el.html(template);
                    armies.each(function(army){
                        view = new ArmyListView({model: army});
                        this.$('#armylisttbody').append(view.render({points: points}).el);
                    });
                 }
            });
        }
    });
    return ListView;
});
