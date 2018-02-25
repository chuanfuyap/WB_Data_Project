$(function() {
  $('#economy_plot').click(function() {
                        $.getJSON($SCRIPT_ROOT + '/_plot_economy', {
                                  econ_indicator: $('#econoplot').val()
                                  }, function(data) {
                                  $('#econ_graph').html(data.graph);
                                  $('#econ_script').html(data.script);
                                  });
                        });
  
  
  $('#economy_regionplot').click(function() {
                           $.getJSON($SCRIPT_ROOT + '/_plot_economyregion', {
                                     econ_indicator: $('#econoplot').val(),
                                     region:  $('#econ_region').val()
                                
                                     }, function(data) {
                                     $('#econ_graph').html(data.graph);
                                     $('#econ_script').html(data.script);
                                     });
                           });
  
  $('#economy_countryplot').click(function() {
                           $.getJSON($SCRIPT_ROOT + '/_plot_economycountry', {
                                     econ_indicator: $('#econoplot').val(),
                                     country:  $('#econ_country').val()
                                     }, function(data) {
                                     $('#econ_graph').html(data.graph);
                                     $('#econ_script').html(data.script);
                                     });
                           });
  
  
  
  
  
  
  
  
  
  
  
  $('#health_plot').click(function() {
                   $.getJSON($SCRIPT_ROOT + '/_plot_health', {
                             health_indicator: $('#healthplot').val()
                             }, function(data) {
                             $('#health_graph').html(data.graph);
                             $('#health_script').html(data.script);
                             });
                   });
  
  
  $('#health_regionplot').click(function() {
                                 $.getJSON($SCRIPT_ROOT + '/_plot_healthregion', {
                                           indicator: $('#healthplot').val(),
                                           region:  $('#health_region').val()
                                           
                                           }, function(data) {
                                           $('#health_graph').html(data.graph);
                                           $('#health_script').html(data.script);
                                           });
                                 });
  
  $('#health_countryplot').click(function() {
                                  $.getJSON($SCRIPT_ROOT + '/_plot_healthcountry', {
                                            indicator: $('#healthplot').val(),
                                            country:  $('#health_country').val()
                                            }, function(data) {
                                            $('#health_graph').html(data.graph);
                                            $('#health_script').html(data.script);
                                            });
                                  });
  
  
  
  
  
  
  
  $('#education_plot').click(function() {
                          $.getJSON($SCRIPT_ROOT + '/_plot_edu', {
                                    edu_indicator: $('#eduplot').val()
                                    }, function(data) {
                                    $('#edu_graph').html(data.graph);
                                    $('#edu_script').html(data.script);
                                    });
                          });
  $('#education_regionplot').click(function() {
                                $.getJSON($SCRIPT_ROOT + '/_plot_eduregion', {
                                          indicator: $('#eduplot').val(),
                                          region:  $('#edu_region').val()
                                          
                                          }, function(data) {
                                          $('#edu_graph').html(data.graph);
                                          $('#edu_script').html(data.script);
                                          });
                                });
  
  $('#education_countryplot').click(function() {
                                 $.getJSON($SCRIPT_ROOT + '/_plot_educountry', {
                                           indicator: $('#eduplot').val(),
                                           country:  $('#edu_country').val()
                                           }, function(data) {
                                           $('#edu_graph').html(data.graph);
                                           $('#edu_script').html(data.script);
                                           });
                                 });
  
  
  
  
  
  
  
  
  
  $('#environment_plot').click(function() {
                             $.getJSON($SCRIPT_ROOT + '/_plot_env', {
                                       indicator: $('#envplot').val()
                                       }, function(data) {
                                       $('#env_graph').html(data.graph);
                                       $('#env_script').html(data.script);
                                       });
                             });
  $('#environment_regionplot').click(function() {
                                   $.getJSON($SCRIPT_ROOT + '/_plot_envregion', {
                                             indicator: $('#envplot').val(),
                                             region:  $('#env_region').val()
                                             
                                             }, function(data) {
                                             $('#env_graph').html(data.graph);
                                             $('#env_script').html(data.script);
                                             });
                                   });
  
  $('#environment_countryplot').click(function() {
                                    $.getJSON($SCRIPT_ROOT + '/_plot_envcountry', {
                                              indicator: $('#envplot').val(),
                                              country:  $('#env_country').val()
                                              }, function(data) {
                                              $('#env_graph').html(data.graph);
                                              $('#env_script').html(data.script);
                                              });
                                    });
  
  
  
  
  
  
  
  
  $('#finance_plot').click(function() {
                               $.getJSON($SCRIPT_ROOT + '/_plot_fin', {
                                         indicator: $('#finplot').val()
                                         }, function(data) {
                                         $('#fin_graph').html(data.graph);
                                         $('#fin_script').html(data.script);
                                         });
                               });
  $('#finance_regionplot').click(function() {
                                     $.getJSON($SCRIPT_ROOT + '/_plot_finregion', {
                                               indicator: $('#finplot').val(),
                                               region:  $('#fin_region').val()
                                               
                                               }, function(data) {
                                               $('#fin_graph').html(data.graph);
                                               $('#fin_script').html(data.script);
                                               });
                                     });
  
  $('#finance_countryplot').click(function() {
                                      $.getJSON($SCRIPT_ROOT + '/_plot_fincountry', {
                                                indicator: $('#finplot').val(),
                                                country:  $('#fin_country').val()
                                                }, function(data) {
                                                $('#fin_graph').html(data.graph);
                                                $('#fin_script').html(data.script);
                                                });
                                      });
  
  
  
  
  
  
  
  
  
  $('#development_plot').click(function() {
                           $.getJSON($SCRIPT_ROOT + '/_plot_dev', {
                                     indicator: $('#devplot').val()
                                     }, function(data) {
                                     $('#dev_graph').html(data.graph);
                                     $('#dev_script').html(data.script);
                                     });
                           });
  $('#development_regionplot').click(function() {
                                 $.getJSON($SCRIPT_ROOT + '/_plot_devregion', {
                                           indicator: $('#devplot').val(),
                                           region:  $('#dev_region').val()
                                           
                                           }, function(data) {
                                           $('#dev_graph').html(data.graph);
                                           $('#dev_script').html(data.script);
                                           });
                                 });
  
  $('#development_countryplot').click(function() {
                                  $.getJSON($SCRIPT_ROOT + '/_plot_devcountry', {
                                            indicator: $('#devplot').val(),
                                            country:  $('#dev_country').val()
                                            }, function(data) {
                                            $('#dev_graph').html(data.graph);
                                            $('#dev_script').html(data.script);
                                            });
                                  });
  
  
  
  
  
  
  
  
  $('#poverty_plot').click(function() {
                               $.getJSON($SCRIPT_ROOT + '/_plot_pov', {
                                         indicator: $('#povplot').val()
                                         }, function(data) {
                                         $('#pov_graph').html(data.graph);
                                         $('#pov_script').html(data.script);
                                         });
                               });
  $('#poverty_regionplot').click(function() {
                                     $.getJSON($SCRIPT_ROOT + '/_plot_povregion', {
                                               indicator: $('#povplot').val(),
                                               region:  $('#pov_region').val()
                                               
                                               }, function(data) {
                                               $('#pov_graph').html(data.graph);
                                               $('#pov_script').html(data.script);
                                               });
                                     });
  
  $('#poverty_countryplot').click(function() {
                                      $.getJSON($SCRIPT_ROOT + '/_plot_povcountry', {
                                                indicator: $('#povplot').val(),
                                                country:  $('#pov_country').val()
                                                }, function(data) {
                                                $('#pov_graph').html(data.graph);
                                                $('#pov_script').html(data.script);
                                                });
                                      });
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  });
