
/**
 * Simple extension to the String object thtat allow to format a string python style
 * taken from: https://stackoverflow.com/a/4974690/6791579
 */
String.prototype.format = function () {
	var i = 0, args = arguments;
	return this.replace(/{}/g, function () {
		return typeof args[i] != 'undefined' ? args[i++] : '';
	});
};

/**
 * Helper function that will check if a propriety of a section is set or not by confronting
 * it with the following values ["true", "yes", "y", "ok"]
 * @param type: string setting the setting value to check
 */
function checkIfSettingsIsSet(setting) {
	var filterstrings = ['true','yes','y','ok']
	var regex = new RegExp(filterstrings.join("|"), "i")
	return regex.test(setting)
}