/*!
 * bootstrap-fileinput v4.3.3
 * http://plugins.krajee.com/file-input
 *
 * Font Awesome icon theme configuration for bootstrap-fileinput. Requires font awesome assets to be loaded.
 *
 * Author: Kartik Visweswaran
 * Copyright: 2014 - 2016, Kartik Visweswaran, Krajee.com
 *
 * Licensed under the BSD 3-Clause
 * https://github.com/kartik-v/bootstrap-fileinput/blob/master/LICENSE.md
 */
(function ($) {
    "use strict";

    $.fn.fileinputThemes.fa = {
        fileActionSettings: {
            removeIcon: '<i class="fa fa-trash text-danger"></i>',
            uploadIcon: '<i class="fa fa-upload text-info"></i>',
            zoomIcon: '<i class="fa fa-search-plus"></i>',
            dragIcon: '<i class="fa fa-bars"></i>',
            indicatorNew: '<i class="fa fa-hand-o-down text-warning"></i>',
            indicatorSuccess: '<i class="fa fa-check-circle text-success"></i>',
            indicatorError: '<i class="fa fa-exclamation-circle text-danger"></i>',
            indicatorLoading: '<i class="fa fa-hand-o-up text-muted"></i>'
        },
        layoutTemplates: {
            fileIcon: '<i class="fa fa-file kv-caption-icon"></i> '
        },
        previewZoomButtonIcons: {
            prev: '<i class="fa fa-caret-left fa-lg"></i>',
            next: '<i class="fa fa-caret-right fa-lg"></i>',
            toggleheader: '<i class="fa fa-arrows-v"></i>',
            fullscreen: '<i class="fa fa-arrows-alt"></i>',
            borderless: '<i class="fa fa-external-link"></i>',
            close: '<i class="fa fa-remove"></i>'
        },
        previewFileIcon: '<i class="fa fa-file"></i>',
        browseIcon: '<i class="fa fa-folder-open"></i>',
        removeIcon: '<i class="fa fa-trash"></i>',
        cancelIcon: '<i class="fa fa-ban"></i>',
        uploadIcon: '<i class="fa fa-upload"></i>',
        msgValidationErrorIcon: '<i class="fa fa-exclamation-circle"></i> '
    };
})(window.jQuery);
