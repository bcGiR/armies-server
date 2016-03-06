define([
    'jquery',
    'underscore',
    'backbone',
    'text!templates/armylist.html'
], function($, _, Backbone, armyListTemplate){
    var ArmyListView = Backbone.View.extend({
        tagName: "tr",
        render: function(options){
            var that = this;
            this.model.fetch({
                success: function(army){
                    var template = _.template(armyListTemplate)({army: army,
                                                                dateString: options.dateString,
                                                                points: options.points});
                    that.$el.html(template);
                }
            });
            return this;
        },
        events: {
            "click .armylistitem" : "view"
        },
        view: function(ev){
            this.goTo('#/edit/' + this.model.get("id"));
        }
    });
    return ArmyListView;
});
