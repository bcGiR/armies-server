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
        tagName: 'div',
        initialize: function(options) {
            this.options = options;
        },
        render: function(options){
            var that = this;
            var faction_code = this.options.faction_code;
            var faction = this.options.faction;
            var points = this.options.points;
            var data = null;
            var ordering = this.options.ordering;
            if (points) {
                data = $.param({ordering: ordering, faction: faction_code, points: points});
            } else {
                data = $.param({ordering: ordering, faction: faction_code});
            }
            this.collection.fetch({
                data: data,
                success: function(armies){
                    //armies = armies.sortBy(function(m) {return -Date.parse(m.get('created')).getTime()});
                    console.log(armies);
                    var template = _.template(listTemplate)({faction_code: faction_code,
                                                             faction: faction,
                                                             points: points});
                    that.$el.html(template);
                    armies.each(function(army){
                        var view = new ArmyListView({model: army});
                        var date = Date.parse(army.get("created")); 
                        var dateString = date.toString("dddd, MMMM d, yyyy");
                        this.$('#army-list-tbody').append(view.render({dateString: dateString,
                                                                       points: points}).el);
                    });
                 }
            });
        }
    });
    return ListView;
});
