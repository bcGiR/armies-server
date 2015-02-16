define([
    'jquery',
    'underscore',
    'backbone',
    'views/home',
    'views/list',
    'views/edit',
    'views/new',
], function($, _, Backbone, HomeView, ListView, EditView, NewView){
    var AppRouter = Backbone.Router.extend({
        routes: {
            '': 'home',
            'list/:faction_code(/:points)': 'list',
            'edit/:id': 'editList',
            'new': 'newList',

            '*actions': 'defaultAction'
        }
    });
    
    var initialize = function(){
        // Not sure if this is the right place for the prefilter
        $.ajaxPrefilter( function( options, origionalOptions, jqXHR ) {
            options.url = 'http://localhost:8000/api' + options.url;
        });

        var app_router = new AppRouter;

        // Extending View class to include a navigation method goTo
        Backbone.View.prototype.goTo = function(loc){
            app_router.navigate(loc, {trigger: true});
        };

        app_router.on('route:home', function(){
            var homeView = new HomeView();
            homeView.render();
        });
        app_router.on('route:list', function(faction_code, points){
            var listView = new ListView();
            listView.render({faction_code: faction_code,
                             points: points});
        });
        app_router.on('route:editList', function(id){
            var editView = new EditView();
            editView.render({id: id});
        });
        app_router.on('route:newList', function() {
            var newView = new NewView();
            newView.render();
        });
        Backbone.history.start();
    };
    return {
        initialize: initialize
    };
});
