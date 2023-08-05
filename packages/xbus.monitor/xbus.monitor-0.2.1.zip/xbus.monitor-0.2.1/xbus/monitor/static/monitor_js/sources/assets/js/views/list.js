Views.list = Backbone.View.extend({
    el: '#ajax-content',
    events: {
        'submit .add-select': 'addRecord',
        'click .delete': 'deleteRecord'
    },

    initialize: function(options) {
        console.log('listview initialize', this.collection);

        var self = this;

        this.collection.view = this;

        // Settings influencing the collection URL.
        // Use URI.js to parse default parameters.
        // <http://medialize.github.io/URI.js/>
        this.initial_url_params = options.params ? URI
            .parseQuery(options.params) : {};
        this.filters = this.collection.default_filters;
        if (this.filters) {
            // TODO Use <https://lodash.com/docs#cloneDeep> for the deep copy.
            this.filters = $.extend(true, {}, this.filters);
        }
        this.updateCollectionUrl();

        this.id = options.id;
        this.rel = options.rel;
        this.template = options.template;
        this.render(); // Pre-render before refreshing anything.
        this.collection.fetch({
            success: function() {
                self.listenTo(self.collection, 'sync', self.render);
                self.render();
            }
        });
    },

    removeReferences: function() {
        /* Make sure this view is no longer linked to its collection. */
        this.collection.view = null;
    },

    render: function() {
        console.log('collection view render');
        this.$el.html(this.template({
            filters: this.filters,
            models: this.collection.models,
            name: this.collection.name,
            pagination: this.renderPagination(),
            rel_name: this.rel ? this.collection.rel_name
                : this.collection.name,
            id: this.id,
            rel: this.rel
        }));
        return this;
    },

    renderPagination: function() {
        /*
         * Fill the "pagination" template to add pagination controls below the
         * list.
         * 
         * Logarithmic pagination - from <http://stackoverflow.com/a/14193775>.
         */

        var page = this.collection.state.currentPage;
        var last_page = this.collection.state.totalPages;
        var LINKS_PER_STEP = 3;
        var page_begin = 1;
        var page_end = page;
        var last_page_begin = 1;
        var last_page_end = page;
        var c1 = LINKS_PER_STEP + 1;
        var c2 = LINKS_PER_STEP + 1;
        var step = 1;
        var page_indexes = [];
        var page_indexes_begin = [];
        var page_indexes_end = [];

        while (true) {
            if (c1 >= c2) {
                page_indexes_begin.push(page_begin); // Append.
                last_page_begin = page_begin;
                page_begin += step;
                c1--;
            } else {
                page_indexes_end.splice(0, 0, page_end); // Prepend.
                last_page_end = page_end;
                page_end -= step;
                c2--;
            }
            if (c2 === 0) {
                step *= 10;
                page_begin += step - 1; // Round up to nearest step.
                page_begin -= (page_begin % step);
                page_end -= (page_end % step); // Round down to nearest step.
                c1 = LINKS_PER_STEP;
                c2 = LINKS_PER_STEP;
            }
            if (page_begin > page_end) {
                page_indexes = page_indexes.concat(page_indexes_begin);
                page_indexes = page_indexes.concat(page_indexes_end);
                if ((last_page_end > page) || (page >= last_page))
                    break;
                last_page_begin = page;
                last_page_end = last_page;
                page_begin = page + 1;
                page_end = last_page;
                c1 = LINKS_PER_STEP;
                c2 = LINKS_PER_STEP + 1;
                page_indexes_begin = [];
                page_indexes_end = [];
                step = 1;
            }
        }

        return Templates['pagination']({
            collection: this.collection,
            page_indexes: page_indexes
        });
    },

    updateCollectionUrl: function() {
        /* Make the collection's URL aware of custom settings. */

        var that = this;
        // TODO Use <https://lodash.com/docs#cloneDeep> for the deep copy.
        this.url_params = $.extend(true, {}, this.initial_url_params);
        if (this.filters) {
            _.each(this.filters, function(filter) {
                var field = filter[0], operator = filter[1], value = filter[2];
                value = JSON.stringify(value);
                that.url_params[field + ':' + operator] = value;
            });
        }
    },

    addRecord: function(ev) {
        var that = this;
        var data = Backbone.Syphon.serialize(this);
        var model = new this.collection.model();
        model.set('id', data['new_rel_id']);
        model.save({}, {
            success: function() {
                console.log('record edited', that.id);
                Backbone.history.loadUrl(Backbone.history.fragment);
            }
        });
        return false;
    },

    deleteRecord: function(ev) {
        var that = this;
        var model = new this.collection.model();
        model.set('id', $(ev.target).attr('value'));
        model.destroy({
            success: function() {
                console.log('record removed/deleted', that.id);
                Backbone.history.loadUrl(Backbone.history.fragment);
            }
        });
    }
});

function applyFilter(el, field) {
    /* Update the filter the view is using and reload its contents. */

    var node = $(el);
    var value = node.val();

    var filter = [];

    if (value !== null) {
        switch (el.tagName) {
        case 'SELECT':
            var operator = el.multiple ? 'in' : 'eq';
            filter = [field, operator, value];
            break;
        default:
            alert(el.tagName + ' controls are not supported yet.');
            break;
        }
    }

    main_view.filters[el.name] = filter;

    main_view.updateCollectionUrl();
    main_view.collection.fetch();
}

function switchPage(page_index) {
    /*
     * Load results in the specified page; render the view once they have been
     * retrieved.
     */

    main_view.collection.getPage(page_index, {
        success: function() {
            main_view.render();
        }
    });
}

function switchToNextPage() {
    /*
     * Load results in the next page; render the view once they have been
     * retrieved.
     */

    main_view.collection.getNextPage({
        success: function() {
            main_view.render();
        }
    });
}

function switchToPrevPage() {
    /*
     * Load results in the previous page; render the view once they have been
     * retrieved.
     */

    main_view.collection.getPreviousPage({
        success: function() {
            main_view.render();
        }
    });
}
