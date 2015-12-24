var catalogApp = angular.module('catalogApp', ['ngRoute', 'mgcrea.ngStrap']);

//routes
catalogApp.config(['$routeProvider', 
	function($routeProvider){
		$routeProvider.
			when('/', {
				templateUrl:'static/client/components/landing/landing.html',
				controller:'landingCtrl'
			}).
			when('/browse/:categoryId?', {
				templateUrl:'static/client/components/browse/browse.html',
				controller:'browseCtrl'
			}).
			when('/profile', {
				templateUrl:'static/client/components/profile/profile.html',
				controller:'profileCtrl'
			}).
			
			otherwise({
				redirectTo: '/'
			});
	}]);