(function () {
'use strict';

angular

.module('worldCountries', ['ngResource'])

.factory('Country', function($resource) {
    return $resource(
        '/api/countries/:id', {id: '@id'},
        {
            all: {method: 'GET', url: '/api/countries/?format=json', isArray:true}
        }
    );
})

.controller('IndexController', function ($scope, Country) {
    $scope.countries = Country.all();
});

})();
