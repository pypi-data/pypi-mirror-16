jQuery(document).ready(function($) {

  var format = function(state) {
      var option = $(state.element);
      return '<span class="' + option.data('css') + '">' + state.text + '</span>';
  };

  $('.single-select2-widget').select2({
      width: 'resolve',
      formatResult: format,
      formatSelection: format,
      escapeMarkup: function(m) { return m; },
  });

  $('.multi-select2-widget').select2({
    formatResult: format,
    formatSelection: format,
    escapeMarkup: function(m) { return m; },
  });

});
