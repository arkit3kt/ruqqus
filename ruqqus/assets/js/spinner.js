$(document).ready(function() {
	$('#login_form').submit(function() {
      // disable button
      $("#login_button").prop("disabled", true);
      // add spinner to button
      $("#login_button").html(
        `<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Signing in`
      );
    });
});

$(document).ready(function() {
	$('#register_form').submit(function() {
      // disable button
      $("#login_button").prop("disabled", true);
      // add spinner to button
      $("#login_button").html(
        `<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Registering`
      );
    });
});

$(document).ready(function() {
	$('#submit_form').submit(function() {
      // disable button
      $("#submit_button").prop("disabled", true);
      // add spinner to button
      $("#submit_button").html(
        `<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Creating post`
      );
    });
});