define([
    'underscore',
    'backbone',
    'models/army'
], function(_, Backbone, ArmyModel){
    var ArmyCollection = Backbone.Collection.extend({
        url: '/armylists'
    });
    return ArmyCollection;
});
