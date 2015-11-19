catalogApp.controller('browseCtrl', ['$scope', '$routeParams',
	function($scope, $routeParams){

		$scope.categoryId = $routeParams.categoryId;
		if($scope.categoryId) {$scope.browseAll = false;}
		else {$scope.browseAll = true;}
	}])