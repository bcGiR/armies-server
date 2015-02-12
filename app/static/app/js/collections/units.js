define([
    'underscore',
    'backbone',
    'models/unit'
], function(_, Backbone, UnitModel){
    var UnitCollection = Backbone.Collection.extend({
        url: '/units'
    });
    return UnitCollection;
});
