
/**
 * Simple extension to the String object that allow to format a string python style
 * taken from `StackOverflow <https://stackoverflow.com/a/4974690/6791579>`_
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
 * @param {String} setting String value to check
 */
function checkIfSettingsIsSet(setting) {
	var filterstrings = ['true','yes','y','ok']
	var regex = new RegExp(filterstrings.join("|"), "i")
	return regex.test(setting)
}

/**
 * Filter the Megascan Asset list removing a speific asset
 * @param  {Object} asset the asset to remove
 * @param  {Array} assets the list of asset to filter
 */
function removeFromAssets(asset, assets) {
	return assets.filter(function (element) {
		return element.id != asset.id
	})
}