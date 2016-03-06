define([], function() {

    function AppView() {};
    
    AppView.prototype.showView = function(view) {
            if (this.currentView) {
                this.currentView.close();
            }

            this.currentView = view;
            this.currentView.render();

            $(".page").html(this.currentView.el);

    };

    return AppView;

});
