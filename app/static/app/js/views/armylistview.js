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
            var points = options.points;
            var army = that.model;
            army.fetch({
                success: function(army){
                    console.log('success');
                    var template = _.template(armyListTemplate)({army: army,
                                                                points: points});
                    that.$el.html(template);
                }
            });
            return this;
        }
    });
    return ArmyListView;
});
