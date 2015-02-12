define([
    'underscore',
    'backbone',
    'models/army'
], function(_, Backbone, ListEntryModel){
    var ListEntryCollection = Backbone.Collection.extend({
        url: '/listentry'
    });
    return ListEntryCollection;
});
