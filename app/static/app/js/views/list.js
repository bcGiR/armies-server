define([
    'jquery',
    'underscore',
    'backbone',
    'collections/armies',
    'views/armylistview',
    'util/date',
    'text!templates/list.html'
], function($, _, Backbone, ArmyCollection, ArmyListView, date, listTemplate){
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
                        var view = new ArmyListView({model: army});
                        var date = Date.parse(army.get("created")); 
                        var dateString = date.toString("dddd, MMMM d, yyyy");
                        this.$('#army-list-tbody').append(view.render({dateString: dateString,
                                                                       points: options.points}).el);
                    });
                 }
            });
        }
    });
    return ListView;
});
