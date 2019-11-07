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