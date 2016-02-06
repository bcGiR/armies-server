define([
    'jquery',
    'underscore',
    'backbone',
    'collections/armies',
    'views/armylistview',
    'text!templates/list.html'
], function($, _, Backbone, ArmyCollection, ArmyListView, listTemplate){
    var ListView = Backbone.View.extend({
        el: '.page',
        render: function(options){
            var that = this;
            this.collection.fetch({
                data: options.data,
                success: function(armies){
                    var template = _.template(listTemplate)({faction_code: options.faction_code,
                                                             faction: options.faction,
                                                             points: options.points});
                    that.$el.html(template);
                    armies.each(function(army){
                        view = new ArmyListView({model: army});
                        this.$('#army-list-tbody').append(view.render({points: options.points}).el);
                    });
                 }
            });
        }
    });
    return ListView;
});
