(function () {
'use strict';

angular.module('worldCountries', ['ngResource', 'ngRoute'])

.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'static/js/pages/list.html',
                controller: 'ListController'
            })
            .when('/top5', {
                templateUrl: 'static/js/pages/list.html',
                controller: 'Top5Controller'
            })
            .when('/details/:id', {
                templateUrl: 'static/js/pages/details.html',
                controller: 'DetailsController'
            })
            .otherwise({
                redirectTo: '/'
            });
    }
])

.factory('Country', function($resource) {
    return $resource(
        '/api/countries/:id', {id: '@id'},
        {
            all: {method: 'GET', url: '/api/countries/', isArray: true},
            top5: {method: 'GET', url: '/api/countries/', params: {page_size: 5, ordering: '-population'}}
        }
    );
})

.controller('ListController', function ($scope, Country) {
    $scope.pageHeader = 'Countries list';
    $scope.countries = Country.all();
})

.controller('Top5Controller', function ($scope, Country) {
    $scope.pageHeader = 'Top 5 most populated countries';
    Country.top5({}, function (result) {
        $scope.countries = result.results;
    });
})

.controller('DetailsController', function ($scope, $routeParams, Country) {
    Country.get({id: $routeParams.id}, function (result) {
        $scope.country = result;
    });
});

})();
