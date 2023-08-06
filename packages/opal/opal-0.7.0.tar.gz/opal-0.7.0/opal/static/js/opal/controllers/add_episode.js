angular.module('opal.controllers')
    .controller(
        'AddEpisodeCtrl',
        function($scope, $http,
                 $timeout, $routeParams,
                 $modalInstance, $rootScope,
                 Episode, FieldTranslater, Referencedata,
                 TagService,
                 referencedata,
                 demographics,
                 tags){
            "use strict";
            var currentTags = [];

            _.extend($scope, referencedata.toLookuplists());

	        $scope.editing = {
                tagging: [{}],
		        location: {},
                demographics: demographics
	        };

            if(tags.tag){
                currentTags = [tags.tag];
            }

            if(tags.subtag){
                // if there's a subtag, don't tag with the parent tag
                currentTags = [tags.subtag];
            }

            $scope.tagService = new TagService(currentTags);

	        $scope.save = function() {
                $scope.editing.tagging = [$scope.tagService.toSave()];
                var toSave = FieldTranslater.jsToPatient($scope.editing)

		        $http.post('/api/v0.1/episode/', toSave).success(function(episode) {
			        episode = new Episode(episode);
			        $modalInstance.close(episode);
		        });
	        };

	        $scope.cancel = function() {
		        $modalInstance.close(null);
	        };

        });
