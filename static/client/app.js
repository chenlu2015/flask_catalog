var catalogApp = angular.module('catalogApp', ['ngRoute']);

//routes
catalogApp.config(['$routeProvider', 
	function($routeProvider){
		$routeProvider.
			when('/', {
				templateUrl:'static/client/components/landing/landing.html',
				controller:'landingCtrl'
			}).
			when('/profile', {
				templateUrl:'static/client/components/profile/profile.html',
				controller:'profileCtrl'
			}).
			when('/category/:categoryId?', {
				templateUrl:'static/client/components/browse/browse.html',
				controller:'browseCtrl'
			}).
			otherwise({
				redirectTo: '/'
			});
	}]);