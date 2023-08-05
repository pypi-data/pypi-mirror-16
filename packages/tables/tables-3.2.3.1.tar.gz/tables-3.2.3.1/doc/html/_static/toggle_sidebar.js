/*
 * toggle_sidebar.js
 * ~~~~~~~~~~~~~~
 *
 * Sphinx JavaScript helper for collapsible sidebar.
 * adds button into sidebar, and toggles document.collapsed-sidebar
 * all the actual collapsing is done via css.
 *
 * :copyright: Copyright 2011 by Assurance Technologies
 * :license: BSD
 *
 */

$(document).ready(function (){
  var holder = $('<div class="sidebartoggle"><button id="sidebar-hide" title="click to hide the sidebar">&laquo;</button><button id="sidebar-show" style="display: none" title="click to show the sidebar">sidebar &raquo;</button></div>');
  var doc = $('div.document');

  var show_btn = $('#sidebar-show', holder);
  var hide_btn = $('#sidebar-hide', holder);
  var copts = { expires: 7, path: DOCUMENTATION_OPTIONS.url_root };

  show_btn.click(function (){
    doc.removeClass("collapsed-sidebar");
    hide_btn.show();
    show_btn.hide();
    $.cookie("sidebar", "expanded", copts);
  });

  hide_btn.click(function (){
    doc.addClass("collapsed-sidebar");
    show_btn.show();
    hide_btn.hide();
    $.cookie("sidebar", "collapsed", copts);
  });

  var state = $.cookie("sidebar");
  if(!state && false){
   state = "collapsed";
  }

  doc.append(holder);

  if (state == "collapsed"){
    doc.addClass("collapsed-sidebar");
    show_btn.show();
    hide_btn.hide();
  }

});