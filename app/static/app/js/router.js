define([
    'jquery',
    'underscore',
    'backbone',
    'views/home',
    'views/list',
    'views/edit',
    'views/new',
    'collections/armies',
    'util/factioncode',
    'util/appview'
], function($, _, Backbone, HomeView, ListView, EditView, NewView, ArmyCollection, FactionCode, AppView){
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
        var appView = new AppView;

        // Extending View class to include a navigation method goTo
        Backbone.View.prototype.goTo = function(loc){
            app_router.navigate(loc, {trigger: true});
        };
        Backbone.View.prototype.close = function() {
            this.remove();
            this.unbind();
            if (this.onClose) {
                this.onClose();
            }
        }

        app_router.on('route:home', function(){
            var homeView = new HomeView();
            appView.showView(homeView);
        });
        app_router.on('route:list', function(faction_code, points){
            var data = null;
            if (points) {
                data = $.param({faction: faction_code, points: points});
            } else {
                data = $.param({faction: faction_code});
            }
            var faction = FactionCode.getFaction(faction_code);
            var armies = new ArmyCollection();
            var listView = new ListView({collection: armies,
                                         faction: faction,
                                         faction_code: faction_code,
                                         points: points});
            appView.showView(listView);
        });
        app_router.on('route:editList', function(id){
            var editView = new EditView({id: id});
            appView.showView(editView);
        });
        app_router.on('route:newList', function() {
            var newView = new NewView();
            appView.showView(newView);
        });
        Backbone.history.start();
    };
    return {
        initialize: initialize
    };
});
