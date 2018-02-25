$(function() {
  $('#model_economy').click(function() {
                           $.getJSON($SCRIPT_ROOT + '/_model_econ', {
                                     a1: $('#econ_1').val(),
                                     a2: $('#econ_2').val(),
                                     a3: $('#econ_3').val(),
                                     a4: $('#econ_4').val(),
                                     a5: $('#econ_5').val(),
                                     a6: $('#econ_6').val(),
                                     a7: $('#econ_7').val(),
                                     a8: $('#econ_8').val(),
                                     a9: $('#econ_9').val(),
                                     a10: $('#econ_10').val()
                                     }, function(data) {
                                     $('#econ_output').html(data.output);
                                     });
                           });
  
  $('#model_finance').click(function() {
                            $.getJSON($SCRIPT_ROOT + '/_model_fin', {
                                      a1: $('#fin_1').val(),
                                      a2: $('#fin_2').val(),
                                      a3: $('#fin_3').val(),
                                      a4: $('#fin_4').val(),
                                      a5: $('#fin_5').val(),
                                      a6: $('#fin_6').val(),
                                      a7: $('#fin_7').val(),
                                      a8: $('#fin_8').val(),
                                      a9: $('#fin_9').val(),
                                      a10: $('#fin_10').val()
                                      }, function(data) {
                                      $('#fin_output').html(data.output);
                                      });
                            });
  
  $('#model_development').click(function() {
                                $.getJSON($SCRIPT_ROOT + '/_model_dev', {
                                          a1: $('#dev_1').val(),
                                          a2: $('#dev_2').val(),
                                          a3: $('#dev_3').val(),
                                          a4: $('#dev_4').val(),
                                          a5: $('#dev_5').val(),
                                          a6: $('#dev_6').val(),
                                          a7: $('#dev_7').val(),
                                          a8: $('#dev_8').val(),
                                          a9: $('#dev_9').val(),
                                          a10: $('#dev_10').val()
                                          }, function(data) {
                                          $('#dev_output').html(data.output);
                                          });
                                });
  
  $('#model_poverty').click(function() {
                            $.getJSON($SCRIPT_ROOT + '/_model_pov', {
                                      a1: $('#pov_1').val(),
                                      a2: $('#pov_2').val(),
                                      a3: $('#pov_3').val(),
                                      a4: $('#pov_4').val(),
                                      a5: $('#pov_5').val(),
                                      a6: $('#pov_6').val(),
                                      a7: $('#pov_7').val(),
                                      a8: $('#pov_8').val(),
                                      a9: $('#pov_9').val(),
                                      a10: $('#pov_10').val()
                                      }, function(data) {
                                      $('#pov_output').html(data.output);
                                      });
                            });
  
  
  
  
  
  
  
  
  
  
  
  
  });
