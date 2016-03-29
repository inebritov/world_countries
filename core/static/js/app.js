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
            .otherwise({
                redirectTo: '/'
            });
    }
])

.factory('Country', function($resource) {
    return $resource(
        '/api/countries/:id', {id: '@id'},
        {
            all: {method: 'GET', url: '/api/countries/', isArray:true}
        }
    );
})

.controller('ListController', function ($scope, Country) {
    $scope.pageHeader = 'Countries list';
    $scope.countries = Country.all();
});

})();
