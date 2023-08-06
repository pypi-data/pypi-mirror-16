## -*- coding: utf-8 -*-
<%inherit file="/master/view.mako" />

<%def name="head_tags()">
  ${parent.head_tags()}
  ${h.javascript_link(request.static_url('tailbone:static/js/jquery.ui.tailbone.js'))}
  <script type="text/javascript">
    $(function() {

        $('.newgrid-wrapper').gridwrapper();

        $('#execute-batch').click(function() {
            % if master.has_execution_options:
                $('#execution-options-dialog').dialog({
                    title: "Execution Options",
                    width: 500,
                    height: 300,
                    modal: true,
                    buttons: [
                        {
                            text: "Execute",
                            click: function(event) {
                                $(event.target).button('option', 'label', "Executing, please wait...").button('disable');
                                $('form[name="batch-execution"]').submit();
                            }
                        },
                        {
                            text: "Cancel",
                            click: function() {
                                $(this).dialog('close');
                            }
                        }
                    ]
                });
            % else:
                $(this).button('option', 'label', "Executing, please wait...").button('disable');
                $('form[name="batch-execution"]').submit();
            % endif
        });

    });
  </script>
  <style type="text/css">

    .newgrid-wrapper {
        margin-top: 10px;
    }
    
  </style>
</%def>

<%def name="context_menu_items()">
  ${parent.context_menu_items()}
  % if request.has_perm('{}.csv'.format(permission_prefix)):
      <li>${h.link_to("Download row data as CSV", url('{}.csv'.format(route_prefix), uuid=batch.uuid))}</li>
  % endif
</%def>

<%def name="buttons()">
    <div class="buttons">
      % if not form.readonly and batch.refreshable:
          ${h.submit('save-refresh', "Save & Refresh Data")}
      % endif
      % if not batch.executed and request.has_perm('{}.execute'.format(permission_prefix)):
          <button type="button" id="execute-batch"${'' if execute_enabled else ' disabled="disabled"'}>${execute_title}</button>
      % endif
    </div>
</%def>

<ul id="context-menu">
  ${self.context_menu_items()}
</ul>

<div class="form-wrapper">
  ${form.render(form_id='batch-form', buttons=capture(buttons))|n}
</div><!-- form-wrapper -->

${rows_grid|n}

<div id="execution-options-dialog" style="display: none;">

  ${h.form(url('{}.execute'.format(route_prefix), uuid=batch.uuid), name='batch-execution')}
  % if master.has_execution_options:
      ${rendered_execution_options|n}
  % endif
  ${h.end_form()}

</div>
