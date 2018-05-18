odoo.define('website_seo_semantic_tags.semantic_tags_rte', function (require) {
    'use strict';
    var ajax = require("web.ajax");
    var core = require("web.core");
    var rte  = require('web_editor.rte');
    ajax.loadJS('/website_seo_semantic_tags/static/lib/summernote-semantic-tags.js');

    rte.Class.include({
        // update rte.js config
        config: function ($editable) {
            var config = this._super.apply(this, arguments);
            config.airPopover.splice(0, 1, 
                ['style', ['style', 'strong', 'em', 'mark']]
            );
            config.airPopover.splice(1, 1, 
                ['sem', ['q', 'cite', 'abbr']],
                ['change', ['del', 'ins']],
            );
            config.airPopover.splice(8, 1, 
                ['help', ['clear']],
            );
            return config;
        }
    });


    /* Backend
    * FieldTextHtml Widget 
    * see module 
    * web_editor/static/src/js/backend.js 
    */
});


 
