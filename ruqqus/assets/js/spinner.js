$(document).ready(function() {
	$("#login-form").on("submit", function(){
    $("#login_button").click(function() {
      // disable button
      $(this).prop("disabled", true);
      // add spinner to button
      $(this).html(
        `<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Signing in`
      );
    });
});
});