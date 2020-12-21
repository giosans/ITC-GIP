/*--- Legend window ---*/

'use strict';

Ext.define('CityApp.view.giscientist.LegendWindow', {
  extend: 'Ext.window.Window',
  alias: 'widget.legendwindow',

  layout: 'fit',
  padding: 12,
  border: false,
  header: false,
  closable: false,
  resizable: false,
  style: {
    border: 'solid 1px #cccccc',
  },
});
