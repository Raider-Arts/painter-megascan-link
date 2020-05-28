
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
 * TEst
 */
function importResources(prova) {
	
}