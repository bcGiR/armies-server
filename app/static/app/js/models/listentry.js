define([
    'underscore',
    'backbone'
], function(_, Backbone){
    var ListEntryModel = Backbone.Model.extend({
        urlRoot: '/listentry'
    });
    return ListEntryModel;
});
