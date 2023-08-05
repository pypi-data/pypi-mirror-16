(function ($) {

    var init = function ($element, options) {
        $element.select2(options);
    };

    var initHeavy = function ($element, options) {
        var isLinked = (' ' + $element.attr('class') + ' ').indexOf(' ' + 'django-select2-linked' + ' ') > -1;

        if (isLinked) {
            var linkedFields = $element.data('ajax-LinkedFields').split(' ').filter(Boolean);
            var linkQueryPrefix = $element.data('ajax-LinkQueryPrefix');
            var linkedFieldPrefix = $element.data('ajax-LinkedFieldPrefix');
        }

        var settings = $.extend({
            ajax: {
                data: function (params) {
                    var data = {
                        term: params.term,
                        page: params.page,
                        field_id: $element.data('field_id')
                    }

                    if (isLinked) {
                        linkedFields.forEach(function(item){
                            data[linkQueryPrefix + item] = document.getElementById(linkedFieldPrefix + item).value;
                        });
                    }
                    return data;
                },
                processResults: function (data, page) {
                    return {
                        results: data.results,
                        pagination: {
                            more: data.more
                        }
                    };
                }
            }
        }, options);

        $element.select2(settings);

        if (isLinked) {
            linkedFields.forEach(function(item){
                $('#' + linkedFieldPrefix + item).on('change', function() {
                    if ($element.val() !== null) {
                        $element.select2(settings).val(null).trigger('change');
                    }
                })
            });
        }
    };

    $.fn.djangoSelect2 = function (options) {
        var settings = $.extend({}, options);
        $.each(this, function (i, element) {
            var $element = $(element);
            if ($element.hasClass('django-select2-heavy')) {
                initHeavy($element, settings);
            } else {
                init($element, settings);
            }
        });
        return this;
    };

    $(function () {
        $('.django-select2').djangoSelect2();
    });

}(this.jQuery));
