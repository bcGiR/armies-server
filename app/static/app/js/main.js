require.config({
    paths: {
        jquery: 'libs/jquery/jquery-1.11.2.min',
        underscore: 'libs/underscore/underscore.min',
        backbone: 'libs/backbone/backbone.min',
        templates: '../templates'
    }

});

require([
    'app',
], function(App){
    App.initialize();
});
