define([
    'underscore',
    'backbone'
], function(_, Backbone){
    var UnitModel = Backbone.Model.extend({
        urlRoot: '/units'
    });
    return UnitModel;
});
