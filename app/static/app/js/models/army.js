define([
    'underscore',
    'backbone'
], function(_, Backbone){
    var ArmyModel = Backbone.Model.extend({
        urlRoot: '/armylists'
    });
    return ArmyModel;
});
