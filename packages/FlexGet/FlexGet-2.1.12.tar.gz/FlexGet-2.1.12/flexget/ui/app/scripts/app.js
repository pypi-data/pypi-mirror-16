'use strict';

if (typeof String.prototype.startsWith !== 'function') {
    String.prototype.startsWith = function (prefix) {
        return this.indexOf(prefix) === 0;
    };
}

if (typeof String.prototype.endsWith !== 'function') {
    String.prototype.endsWith = function (suffix) {
        return this.indexOf(suffix, this.length - suffix.length) !== -1;
    };
}

function registerPlugin(plugin) { // eslint-disable-line no-unused-vars
    angular.module('flexget').requires.push(plugin.name);
}

(function () {
  'use strict';

  angular
  .module('flexget', [
    'ui.router',
    'ngMaterial',
    'ngCookies',
    'ngMessages',
    'angular-loading-bar',
    'flexget.components',
    'flexget.directives',
    'flexget.services',
    'angular-cache'
  ]);

  function bootstrapApplication() {
    /* Bootstrap app after page has loaded which allows plugins to register */
    angular.element(document).ready(function () {
      angular.bootstrap(document, ['flexget']);
    });
    window.loadingScreen.finish();
  }

  bootstrapApplication();
})();

(function () {
    'use strict';

    var seriesModule = angular.module('flexget.plugins.series', []);
    registerPlugin(seriesModule);

    seriesModule.run(["$state", "route", "sideNav", "toolBar", function ($state, route, sideNav, toolBar) {
        route.register('series', '/series', 'series-view');

        sideNav.register('/series', 'Series', 'fa fa-tv', 40);
    }]);

})();

(function () {
    'use strict';

    seriesUpdateController.$inject = ["showId", "params", "$mdDialog", "$http"];
    angular
    .module('flexget.plugins.series')
    .controller('seriesUpdateController', seriesUpdateController)
    .directive('unique', uniqueDirective)

    function seriesUpdateController(showId, params, $mdDialog, $http) {
        var vm = this;

        //Copy so we don't override the original items
        vm.params = angular.copy(params);
        vm.newName = undefined;

        vm.cancel = function() {
            $mdDialog.hide();
        }

        vm.removeName = function(index) {
            vm.params.alternate_names.splice(index, 1);
        }

        vm.addName = function() {
            console.log('trying to add');
            if(vm.params.alternate_names.indexOf(vm.newName) == -1) {
                vm.params.alternate_names.push(vm.newName);
                vm.newName = undefined;
            }
        }

        vm.save = function() {
            if(!angular.equals(vm.params, params)) {
                $http.put('/api/series/' + showId, vm.params)
                .success(function(data) {
                    $mdDialog.hide(data);
                })
                .error(function(err) {
                    //TODO: Error handling
                    console.log(err);
                });
            } else {
                $mdDialog.hide();
            }
        }
    }

    function uniqueDirective() {
        return {
            restrict: 'A',
            require: 'ngModel',
            link: function(scope, element, attrs, ctrl) {
                ctrl.$validators.unique = function(modelValue, viewValue) {
                    if(scope.$eval(attrs.uniqueArray).indexOf(viewValue) == -1) {
                        console.log('ok');
                        return true;
                    }
                    return false;
                }
            }
        }
    }
})();

(function () {
    'use strict';

seriesShowController.$inject = ["$state", "$mdDialog", "$http", "seriesService"];
    angular
    .module('flexget.plugins.series')
    .component('seriesShow', {
        templateUrl: 'plugins/series/components/series-show/series-show.tmpl.html',
        controllerAs: 'vm',
        controller: seriesShowController,
        bindings: {
            show: '<',
            forgetShow: '&'
        },
        transclude: true
    });

    function seriesShowController($state, $mdDialog, $http, seriesService) {
        var vm = this;

        //Dialog for the update possibilities, such as begin and alternate names
        function showDialog(params) {
            return $mdDialog.show({
                controller: 'seriesUpdateController',
                controllerAs: 'vm',
                templateUrl: 'plugins/series/components/series-update/series-update.tmpl.html',
                locals: {
                    showId: vm.show.show_id,
                    params: params
                }
            });
        }

        function loadMetadata() {
            seriesService.getShowMetadata(vm.show)
            .then(function(data) {
                vm.show.metadata = data;
            })
            .catch(function (error) {
                console.error(error);
            })
        }

        loadMetadata();

        //Call from the page, to open a dialog with alternate names
        vm.alternateName = function(ev) {
            var params = {
                alternate_names: vm.show.alternate_names
            }

            showDialog(params).then(function(data) {
                if(data) vm.show.alternate_names = data.alternate_names;
            }, function(err) {
                console.log(err);
            });
        }


        //Cat from the page, to open a dialog to set the begin
        vm.setBegin = function(ev) {
            var params = {
                episode_identifier: vm.show.begin_episode.episode_identifier
            }

            showDialog(params).then(function(data){
                if (data) vm.show.begin_episode = data.begin_episode;
            }, function(err) {
                console.log(err);
            });

            /*$mdDialog.show({
            controller: 'seriesBeginController',
            controllerAs: 'vm',
            templateUrl: 'plugins/series/components/series-begin/series-begin.tmpl.html',
            locals: {
            showId: vm.show.show_id
        }
    }).then(function(data) {
    vm.show.begin_episode = data;
}, function(err) {
console.log(err);
});*/
}

}
})();

(function () {
    'use strict';

    seriesEpisodeController.$inject = ["$mdDialog", "$http", "$stateParams", "$filter"];
    angular
    .module('flexget.plugins.series')
    .component('seriesEpisode', {
        templateUrl: 'plugins/series/components/series-episode/series-episode.tmpl.html',
        controllerAs: 'vm',
        controller: seriesEpisodeController,
        bindings: {
            episode: '<',
            show: '<',
            deleteEpisode: '&',
            resetReleases: '&'
        },
    });

    function seriesEpisodeController($mdDialog, $http, $stateParams, $filter){
        var vm = this;


        vm.showReleases = function () {

            var dialog = {
                template: '<episode-releases show="vm.show" episode="vm.episode" releases="vm.releases"></episode-releases>',
                locals: {
                    show: vm.show,
                    episode: vm.episode,
                    releases: vm.releases
                },
                bindToController: true,
                controllerAs: 'vm',
                controller: function () {}
            }

            $mdDialog.show(dialog);

        }

        //Call from the page, to delete all releases
        vm.deleteReleases = function() {
            var confirm = $mdDialog.confirm()
            .title('Confirm deleting releases.')
            .htmlContent("Are you sure you want to delete all releases for <b>" + vm.episode.episode_identifier + "</b> from show <b>" + vm.show.show_name + "</b>?<br /> This also removes all seen releases for this episode!")
            .ok("Forget")
            .cancel("No");

            $mdDialog.show(confirm).then(function() {
                $http.delete('/api/series/' + vm.show.show_id + '/episodes/' + vm.episode.episode_id + '/releases', { params: { forget: true}})
                .success(function(data) {
                    //Remove all loaded releases from the page and set variables for the accordion
                    vm.releases = undefined;
                })
                .error(function(error) {
                    var errorDialog = $mdDialog.alert()
                    .title("Something went wrong")
                    .htmlContent("Oops, something went wrong when trying to forget <b>" + vm.episode.episode_identifier + "</b> from show " + vm.show.show_name + ":<br />" + error.message)
                    .ok("Ok");

                    $mdDialog.show(errorDialog);
                });
            });
        }

    }
})();

(function () {
    'use strict';

    episodesReleasesController.$inject = ["$http", "$filter", "$mdDialog", "seriesService"];
    angular
		.module('flexget.plugins.series')
		.component('episodeReleases', {
			templateUrl: 'plugins/series/components/episode-releases/episode-releases.tmpl.html',
			controllerAs: 'vm',
			controller: episodesReleasesController,
			bindings: {
				show: '<',
				episode: '<',
				releases: '<'
			},
		});


    function episodesReleasesController($http, $filter, $mdDialog, seriesService) {
        var vm = this;
		vm.cancel = cancel;

        loadReleases();

        //Call from a release item, to reset the release
        vm.resetRelease = function (release) {

            var confirm = $mdDialog.confirm()
				.title('Confirm resetting a release')
				.htmlContent("Are you sure you want to reset the release <b>" + release.release_title + "</b>?")
				.ok("reset")
				.cancel("No");

            $mdDialog.show(confirm).then(function () {
                seriesService.resetRelease(vm.show, vm.episode, release).then(function (data) {
                    //Find all downloaded releases, and set their download status to false, which will make the downloaded icon disappear
                    //$filter('filter')(vm.releases, { release_id: id})[0].release_downloaded = false;
                })
            })

        }

        //Call from a release item, to forget the release
        vm.forgetRelease = function (release) {
            var confirm = $mdDialog.confirm()
				.title('Confirm forgetting a release')
				.htmlContent("Are you sure you want to delete the release <b>" + release.release_title + "</b>?")
				.ok("Forget")
				.cancel("No");

            $mdDialog.show(confirm).then(function () {
                seriesService.forgetRelease(vm.show, vm.episode, release).then(function (data) {
                    //Find index of the release and remove it from the list
                    var index = vm.releases.indexOf(release);
                    vm.releases.splice(index, 1);

                    vm.episode.episode_number_of_releases -= 1;
                    if (vm.releases.length == 0) {
                        vm.releases = undefined;
                    }
                })
            })
        }

        function loadReleases() {
            $http.get('/api/series/' + vm.show.show_id + '/episodes/' + vm.episode.episode_id + '/releases')
				.success(function (data) {
					vm.releases = data.releases;

				}).error(function (error) {
					console.log(error);
				});
        }

		function cancel() {
			$mdDialog.cancel();
		}
    }
})();

(function () {
  'use strict';

  var seenModule = angular.module(
    'flexget.plugins.seen',
    ['schemaForm']
  );

  registerPlugin(seenModule);

  seenModule.run(["route", "sideNav", function run(route, sideNav) {
    route.register('seen', '/seen', 'seen-view');
    sideNav.register('/seen', 'Seen', 'fa fa-eye', 228);
  }]);
})();

(function () {
  'use strict';

  angular
    .module('flexget.plugins.seen')
    .component('seenFields',{
      templateUrl: 'plugins/seen/compnents/seen-fields/seen-fields.tmpl.html',
      controllerAs: 'vm',
      controller: seenFieldsController,
      bindings: {
        fields: '<',
      },
    });

  function seenFieldsController() {
  }
})();

(function () {
  'use strict';

  angular
    .module('flexget.plugins.seen')
    .component('seenEntry',{
      templateUrl: 'plugins/seen/components/seen-entry/seen-entry.tmpl.html',
      controllerAs: 'vm',
      bindings: {
        entry: '<',
      },
    });
})();

(function () {
    'use strict';

    var moviesModule = angular.module("flexget.plugins.movies", []);

    registerPlugin(moviesModule);

    moviesModule.run(["route", "sideNav", function (route, sideNav) {
        route.register('movies', '/movies', 'movies-view');
        sideNav.register('/movies', 'Movies', 'fa fa-film', 50);
    }]);

})();

(function () {
  'use strict';

  newListController.$inject = ["moviesService", "$mdDialog"];
  angular
    .module('flexget.plugins.movies')
    .controller('newListController', newListController);

  function newListController(moviesService, $mdDialog) {
    var vm = this;

    vm.saveList = saveList;
    vm.cancel = cancel;

    function cancel() {
      $mdDialog.cancel();
    };

    function saveList() {
      moviesService.createList(vm.listName).then(function (newList) {
        $mdDialog.hide(newList);
      });
    }
  };
})();
(function () {
  'use strict';

  movieEntryController.$inject = ["$http"];
  angular
  .module('flexget.plugins.movies')
  .component('movieEntry',{
    templateUrl: 'plugins/movies/components/movie-entry/movie-entry.tmpl.html',
    controller: movieEntryController,
    controllerAs: 'vm',
    bindings: {
      movie: '<',
      deleteMovie: '&'
    },
  });


  function movieEntryController ($http) {

    var vm = this;

    getMetadata();


    function getMetadata() {

      var params = {
        year : vm.movie.year
      }

      vm.movie.movies_list_ids.forEach(function (id) {
        var newid = {};
        newid[id.id_name] = id.id_value;
        params = $.extend(params, newid);
      })


      $http.get('/api/trakt/movies/' + vm.movie.title + '/', {
        params: params,
        cache: true
      })
      .success(function (data) {

        vm.metadata = data;


      }).error(function (err) {
        console.error(err);
      })
    }
  }



})();

(function () {
  'use strict';

  var executeModule = angular.module("flexget.plugins.execute", ['ui.grid', 'ui.grid.autoResize', 'angular-spinkit']);

  registerPlugin(executeModule);

  executeModule.run(["route", "sideNav", function (route, sideNav) {
    route.register('execute', '/execute', 'execute-view');
    sideNav.register('/execute', 'Execute', 'fa fa-cog', 20);
  }]);

})();

(function () {
  'use strict';

  angular
    .module('flexget.plugins.execute')
    .component('executeStream', {
      templateUrl: 'plugins/execute/components/execute-stream/execute-stream.tmpl.html',
      controllerAs: 'vm',
      bindings: {
        stream: '<',
        running: '<',
        clear: '<',
      },
    });
})();

(function () {
  'use strict';

  angular
    .module('flexget.plugins.execute')
    .component('executeInput', {
      templateUrl: 'plugins/execute/components/execute-input/execute-input.tmpl.html',
      controllerAs: 'vm',
      bindings: {
        options: '<',
        running: '<',
        execute: '<',
        tasksInput: '<',
        addTask: '<',
      },
    });
})();

(function() {
    'use strict';

    angular
        .module('flexget.services', [
        ]);
})();
(function () {
    'use strict';

    serverService.$inject = ["$http"];
    angular.module('flexget.services')
        .service('server', serverService);

    function serverService($http) {
        this.reload = function () {
            return $http.get('/api/server/reload/');
        };

        this.shutdown = function () {
            return $http.get('/api/server/shutdown/')
        };
    }

})();



(function () {
    'use strict';

    serverConfig.$inject = ["toolBar", "server", "$mdDialog"];
    angular.module('flexget.services')
        .run(serverConfig);

    function serverConfig(toolBar, server, $mdDialog) {

        var reload = function () {
            var reloadController = function ($mdDialog) {
                var vm = this;

                vm.title = 'Reload Config';
                vm.showCircular = true;
                vm.content = null;
                vm.buttons = [];
                vm.ok = null;

                vm.hide = function () {
                    $mdDialog.hide();
                };

                var done = function (text) {
                    vm.showCircular = false;
                    vm.content = text;
                    vm.ok = 'Close';
                };

                server.reload()
                    .success(function () {
                        done('Reload Success');
                    })
                    . error(function (data, status, headers, config) {
                        done('Reload failed: ' + data.error);
                    });
            };
            reloadController.$inject = ["$mdDialog"];

            $mdDialog.show({
                templateUrl: 'services/modal/modal.dialog.circular.tmpl.html',
                parent: angular.element(document.body),
                controllerAs: 'vm',
                controller: reloadController
            });
        };

        var doShutdown = function () {
            window.stop(); // Kill any http connection

            var shutdownController = function ($mdDialog) {
                var vm = this;

                vm.title = 'Shutting Down';
                vm.showCircular = true;
                vm.content = null;
                vm.buttons = [];
                vm.ok = null;

                vm.hide = function () {
                    $mdDialog.hide();
                };

                var done = function (text) {
                    vm.title = 'Shutdown';
                    vm.showCircular = false;
                    vm.content = text;
                    vm.ok = 'Close';
                };

                server.shutdown().
                success(function () {
                    done('Flexget has been shutdown');
                }).
                error(function (error) {
                    done('Flexget failed to shutdown failed: ' + error.message);
                });
            };
            shutdownController.$inject = ["$mdDialog"];
            $mdDialog.show({
                templateUrl: 'services/modal/modal.dialog.circular.tmpl.html',
                parent: angular.element(document.body),
                controllerAs: 'vm',
                controller: shutdownController
            });

        };

        var shutdown = function () {
            $mdDialog.show(
                $mdDialog.confirm()
                    .parent(angular.element(document.body))
                    .title('Shutdown')
                    .content('Are you sure you want to shutdown Flexget?')
                    .ok('Shutdown')
                    .cancel('Cancel')
            ).then(function () {
                doShutdown();
            });

        };

        toolBar.registerMenuItem('Manage', 'Reload', 'fa fa-refresh', reload);
        toolBar.registerMenuItem('Manage', 'Shutdown', 'fa fa-power-off', shutdown);

    }

})();

(function () {
    'use strict';

    modalService.$inject = ["$modal"];
    angular.module('flexget.services')
        .service('modal', modalService);

    function modalService($modal) {

        var defaultOptions = {
            backdrop: true,
            keyboard: true,
            modalFade: true,
            size: 'md',
            templateUrl: 'services/modal/modal.tmpl.html',
            headerText: 'Proceed?',
            bodyText: 'Perform this action?',
            okText: 'Ok',
            okType: 'primary',
            closeText: 'Cancel',
            closeType: 'default'
        };

        this.showModal = function (options) {
            //Create temp objects to work with since we're in a singleton service
            var tempOptions = {};
            angular.extend(tempOptions, defaultOptions, options);

            if (!tempOptions.controller) {
                tempOptions.controller = function ($modalInstance) {
                    vm = this;

                    vm.modalOptions = tempOptions;

                    vm.ok = function (result) {
                        $modalInstance.close(result);
                    };
                    vm.close = function (result) {
                        $modalInstance.dismiss('cancel');
                    };
                }
            }

            tempOptions.controllerAs = 'vm';

            return $modal.open(tempOptions).result;
        };

    }

})();
(function () {
    'use strict';

    seriesService.$inject = ["$http", "CacheFactory", "$mdDialog", "errorService"];
    angular.module('flexget.services')
    .factory('seriesService', seriesService);

    function seriesService($http, CacheFactory, $mdDialog, errorService) {
        // If cache doesn't exist, create it
        if (!CacheFactory.get('seriesCache')) {
            CacheFactory.createCache('seriesCache');
        }

        var seriesCache = CacheFactory.get('seriesCache');

        return {
            getShows: getShows,
            getShowMetadata: getShowMetadata,
            deleteShow: deleteShow,
            searchShows: searchShows,
            getEpisodes: getEpisodes,
            deleteEpisode: deleteEpisode,
            resetReleases: resetReleases,
            forgetRelease: forgetRelease,
            resetRelease: resetRelease,
        }

        function getShows(options) {
            return $http.get('/api/series/',
            {
                cache: seriesCache,
                params: options
            })
            .then(getShowsComplete)
            .catch(callFailed);

            function getShowsComplete(response) {
                return response.data;
            }
        }


        function getShowMetadata(show) {
            return $http.get('/api/tvdb/series/' + show.show_name, { cache: true })
            .then(getShowMetadataComplete)
            .catch(callFailed);

            function getShowMetadataComplete(res) {
                return res.data;
            }
        }

        function deleteShow(show) {
            //TODO: Prob add warning messages again

            return $http.delete('/api/series/' + show.show_id,
            {
                params: { forget: true }
            })
            .then(deleteShowComplete)
            .catch(callFailed)

            function deleteShowComplete() {
                // remove all shows from cache, since order might have changed
                seriesCache.removeAll();
                return;
            }
        }

        function searchShows(searchTerm) {
            return $http.get('/api/series/search/' + searchTerm)
            .then(searchShowsComplete)
            .catch(callFailed);

            function searchShowsComplete(response) {
                return response.data;
            }
        }

        function getEpisodes(show, params) {
            return $http.get('/api/series/' + show.show_id + '/episodes', { params: params })
            .then(getEpisodesComplete)
            .catch(callFailed);

            function getEpisodesComplete(res) {
                return res.data;
            }
        }

        function deleteEpisode(show, episode) {
            return $http.delete('/api/series/' + show.show_id + '/episodes/' + episode.episode_id, { params: { forget: true} })
            .then(deleteEpisodeComplete)
            .catch(callFailed)

            function deleteEpisodeComplete(res) {
                return res.data;
            }
        }

        function resetReleases(show, episode) {
            return $http.put('/api/series/' + show.show_id + '/episodes/' + episode.episode_id + '/releases')
            .then(resetReleasesComplete)
            .catch(callFailed)

            function resetReleasesComplete(res) {
                return res.data;
            }
        }

        function forgetRelease(show, episode, release) {
            return $http.delete('/api/series/' + show.show_id + '/episodes/' + episode.episode_id + '/releases/' + release.release_id + '/', { params: { forget: true }})
            .then(forgetReleaseComplete)
            .catch(callFailed);

            function forgetReleaseComplete(res) {
                return res.data;
            }
        }

        function resetRelease(show, episode, release) {
            return $http.put('/api/series/' + show.show_id + '/episodes/' + episode.episode_id + '/releases/' + release.release_id + '/')
            .then(resetReleaseComplete)
            .catch(callFailed);

            function resetReleaseComplete(data) {
                return data;
            }
        }


        function callFailed(error) {
            //TODO: handle error

            console.log(error);

            errorService.showToast(error);
        }

    }
})();

(function () {
    'use strict';

    moviesService.$inject = ["$http", "CacheFactory", "$mdDialog", "errorService"];
    angular.module('flexget.services')
        .factory('moviesService', moviesService);

    function moviesService($http, CacheFactory, $mdDialog, errorService) {
        // If cache doesn't exist, create it
        if (!CacheFactory.get('moviesCache')) {
            CacheFactory.createCache('moviesCache');
        }

        var moviesCache = CacheFactory.get('moviesCache');

        return {
            getLists: getLists,
            deleteList: deleteList,
            getListMovies: getListMovies,
            deleteMovie: deleteMovie,
            createList: createList
        }

        function getLists() {
            return $http.get('/api/movie_list/')
                .then(getListsComplete)
                .catch(callFailed);

            function getListsComplete(response) {
                return response.data;
            }
        }

        function deleteList(listId) {
            return $http.delete('/api/movie_list/' + listId + '/')
                .then(deleteListComplete)
                .catch(callFailed);

            function deleteListComplete(response) {
                return;
            }
        }

        function getListMovies(listId, options) {
            return $http.get('/api/movie_list/' + listId + '/movies/', { params: options })
                .then(getListMoviesComplete)
                .catch(callFailed);

            function getListMoviesComplete(response) {
                return response.data;
            }
        }

        function deleteMovie(listId, movieId) {
            return $http.delete('/api/movie_list/' + listId + '/movies/' + movieId + '/')
                .then(deleteMovieComplete)
                .catch(callFailed);

            function deleteMovieComplete() {

                //TODO: Clear cache
                return;
            }
        }

        function createList(name) {
            return $http.post('/api/movie_list/', { name: name })
                .then(createListComplete)
                .catch(callFailed);

            function createListComplete(response) {
                return response.data;
            };
        };

        function callFailed(error) {
            //TODO: handle error

            console.log(error);

            errorService.showToast(error);
        }
    }
})();
(function () {

    'use strict';

    seriesController.$inject = ["$http", "$mdDialog", "seriesService", "$timeout", "$mdMedia"];
    angular
        .module('flexget.plugins.series')
        .component('seriesView', {
            templateUrl: 'plugins/series/series.tmpl.html',
            controllerAs: 'vm',
            controller: seriesController,
        });

    function seriesController($http, $mdDialog, seriesService, $timeout, $mdMedia) {
        var vm = this;

        var options = {
            page: 1,
            page_size: 10,
            in_config: 'all',
            sort_by: 'show_name'
        }

        vm.searchTerm = "";

        function getSeriesList() {
            seriesService.getShows(options).then(function (data) {
                vm.series = data.shows;

                vm.currentPage = data.page;
                vm.totalShows = data.total_number_of_shows;
                vm.pageSize = data.page_size;
            });
        }

        vm.forgetShow = function (show) {
			var confirm = $mdDialog.confirm()
                .title('Confirm forgetting show.')
                .htmlContent("Are you sure you want to completely forget <b>" + show.show_name + "</b>?<br /> This will also forget all downloaded releases.")
                .ok("Forget")
                .cancel("No");

			$mdDialog.show(confirm).then(function () {
				seriesService.deleteShow(show).then(function (data) {
					getSeriesList();
				});
			});
		};


        /*vm.forgetShow = function (show) {
            //Construct the confirmation dialog
            var confirm = $mdDialog.confirm()
                .title('Confirm forgetting show.')
                .htmlContent("Are you sure you want to completely forget <b>" + show.show_name + "</b>?<br /> This will also forget all downloaded releases.")
                .ok("Forget")
                .cancel("No");

            //Actually show the confirmation dialog and place a call to DELETE when confirmed
            $mdDialog.show(confirm).then(function () {
                $http.delete('/api/series/' + show.show_id, { params: { forget: true } })
                    .success(function (data) {
                        var index = vm.series.indexOf(show);
                        vm.series.splice(index, 1);
                    })
                    .error(function (error) {

                        //Show a dialog when something went wrong, this will change in the future to more generic error handling
                        var errorDialog = $mdDialog.alert()
                            .title("Something went wrong")
                            .htmlContent("Oops, something went wrong when trying to forget <b>" + show.show_name + "</b>:\n" + error.message)
                            .ok("Ok");

                        $mdDialog.show(errorDialog);
                    })
            });
        }*/


        //Call from the pagination to update the page to the selected page
        vm.updateListPage = function (index) {
            options.page = index;

            getSeriesList();
        }


        vm.search = function () {
            if (vm.searchTerm) {
                seriesService.searchShows(vm.searchTerm).then(function (data) {
                    vm.series = data.shows;
                });
            } else {
                options.page = 1;
                getSeriesList();
            }
        }

        vm.showEpisodes = function (show) {
            if (show !== vm.selectedShow) {
                $timeout(function () {
                    vm.selectedShow = show;
                }, 10);
            };
			vm.selectedShow = null;
        }

        vm.hideEpisodes = function () {
            vm.selectedShow = null;
        }

        vm.areEpisodesOnShowRow = function (show, index) {
            if (!show) return false;

            var numberOfColumns = 1;

            if ($mdMedia('gt-md')) numberOfColumns = 2;
            if ($mdMedia('gt-lg')) numberOfColumns = 3;

            var isOnRightRow = true;

            var column = index % numberOfColumns;
            var row = (index - column) / numberOfColumns;


            var showIndex = vm.series.indexOf(show);
            var showColumn = showIndex % numberOfColumns;
            var showRow = (showIndex - showColumn) / numberOfColumns;

            if (row !== showRow) isOnRightRow = false;
            if (column !== numberOfColumns - 1) isOnRightRow = false;
            if (showIndex === index && index === (vm.series.length - 1)) isOnRightRow = true;

            return isOnRightRow;
        }

        //Load initial list of series
        getSeriesList();
    }

})();

(function () {
    'use strict';

    episodesController.$inject = ["$http", "$mdDialog", "seriesService"];
    angular
    .module('flexget.plugins.series')
    .component('seriesEpisodesView', {
        templateUrl: 'plugins/series/series-episodes.tmpl.html',
        controllerAs: 'vm',
        controller: episodesController,
        bindings: {
            show : '<',
        },
        transclude: true
    });

    function episodesController($http, $mdDialog, seriesService) {
        var vm = this;


        var options = {
            page: 1,
            page_size: 10
        }

        //Call from the pagination directive, which triggers other episodes to load
        vm.updateListPage = function(index) {
            options.page = index;

            getEpisodesList();
        }

        //Cal the episodes based on the options
        function getEpisodesList() {
            seriesService.getEpisodes(vm.show, options)
            .then(function(data) {
                //Set the episodes in the vm scope to the loaded episodes
                vm.show.episodes = data.episodes;


                //set vars for the pagination
                vm.currentPage = data.page;
                vm.show.totalEpisodes = data.total_number_of_episodes;
                vm.pageSize = options.page_size;

            })
            .catch(function(error) {
                //TODO: Error handling
                console.log(error);
            });
        }

        //Load initial episodes
        getEpisodesList();

        //action called from the series-episode component
        vm.deleteEpisode = function(episode) {
            var confirm = $mdDialog.confirm()
            .title('Confirm forgetting episode.')
            .htmlContent("Are you sure you want to forget episode <b>" + episode.episode_identifier + "</b> from show <b>" + vm.show.show_name + "</b>?<br /> This also removes all downloaded releases for this episode!")
            .ok("Forget")
            .cancel("No");

            $mdDialog.show(confirm).then(function() {
                seriesService.deleteEpisode(vm.show, episode)
                .then(function(data) {
                    //Find the index of the episode in the data
                    var index = vm.show.episodes.indexOf(episode);
                    //Remove the episode from the list, based on the index
                    vm.show.episodes.splice(index, 1);
                }, function(error) {
                    var errorDialog = $mdDialog.alert()
                    .title("Something went wrong")
                    .htmlContent("Oops, something went wrong when trying to forget <b>" + episode.episode_identifier + "</b> from show " + vm.show.show_name + ":\n" + error.message)
                    .ok("Ok");

                    $mdDialog.show(errorDialog);
                });
            });
        }

        //action called from the series-episode components
        vm.resetReleases = function(episode) {
            var confirm = $mdDialog.confirm()
            .title('Confirm resetting releases.')
            .htmlContent("Are you sure you want to reset downloaded releases for <b>" + episode.episode_identifier + "</b> from show <b>" + vm.show.show_name + "</b>?<br /> This does not remove seen entries but will clear the quality to be downloaded again.")
            .ok("Forget")
            .cancel("No");

            $mdDialog.show(confirm).then(function() {
                seriesService.resetReleases(vm.show, episode)
                .then(function(data) {
                    //TODO: Handle reset releases, remove them from view if they are showm
                }, function(error) {
                    var errorDialog = $mdDialog.alert()
                    .title("Something went wrong")
                    .htmlContent("Oops, something went wrong when trying to reset downloaded releases for <b>" + episode.episode_identifier + "</b> from show " + vm.show.show_name + ":<br />" + error.message)
                    .ok("Ok");

                    $mdDialog.show(errorDialog);
                });
            });
        }
    }

})();

(function () {
  'use strict';

  seenController.$inject = ["$http"];
  angular
    .module('flexget.plugins.seen')
    .component('seenView', {
      templateUrl: 'plugins/seen/seen.tmpl.html',
      controllerAs: 'vm',
      controller: seenController,
    });

  function seenController($http) {
    var vm = this;

    vm.title = 'Seen';

    $http.get('/api/seen/', {params: {max: 20}})
      .success(function handleSeen(data) {
        vm.entries = data.seen_entries;
      })
      .error(function handlerSeenError(data) {
        // log error
      });
  }
})();

(function () {
    'use strict';
    
    var scheduleModule = angular.module('flexget.plugins.schedule', ['schemaForm']);
    registerPlugin(scheduleModule);
    
    scheduleModule.run(["route", "sideNav", function (route, sideNav) {
        route.register('schedule', '/schedule', 'schedule-view');
        sideNav.register('/schedule', 'Schedule', 'fa fa-calendar', 128);
    }]);
    
})();

(function () {
    'use strict';
    
    scheduleController.$inject = ["$http", "schema"];
    angular
        .module('flexget.plugins.schedule')
        .component('scheduleView', {
            templateUrl: 'plugins/schedule/schedule.tmpl.html',
            controllerAs: 'vm',
            controller: scheduleController
        });
    
    function scheduleController($http, schema) {
        var vm = this;
        
        vm.title = 'Schedules';
        vm.description = 'Task execution';
        
        vm.form = [
            '*',
            {
                type: 'submit',
                title: 'Save'
            }
        ];
        
        vm.onSubmit = function (form) {
            // First we broadcast an event so all fields validate themselves
            vm.$broadcast('schemaFormValidate');
            
            // Then we check if the form is valid
            if (form.$valid) {
                alert('test');
                // ... do whatever you need to do with your data.
            }
        };
        
        schema.get('config/schedules').then(function(schema) {
            vm.schema = {type: 'object', 'properties': {'schedules': schema}, required: ['schedules']};
        });
        
        $http.get('/api/schedules/').success(function (data, status, headers, config) {
            vm.models = [data];
        }).error(function (data, status, headers, config) {
            // log error
        });
    }
    
})();

(function () {
    'use strict';

    angular.module('flexget.plugins.movies')
        .filter('moviesListIdsFilter', moviesListIdsFilter);

    function moviesListIdsFilter() {
        var moviesListIds = {
            imdb_id: "IMDB",
            trakt_movie_id: "Trakt",
            tmdb_id: "TMDB"
        };

        return function (id) {
            if (id in moviesListIds) {
                return moviesListIds[id]
            } else {
                return "Unknown Provider: " + id;
            }
        };
    }

})();
(function () {
  'use strict';
  moviesController.$inject = ["$http", "$mdDialog", "$scope", "moviesService"];
  angular
    .module("flexget.plugins.movies")
    .component('moviesView', {
      templateUrl: 'plugins/movies/movies.tmpl.html',
      controllerAs: 'vm',
      controller: moviesController,
    });

  function moviesController($http, $mdDialog, $scope, moviesService) {
    var vm = this;

    var options = {
      page: 1,
      page_size: 10
    }

    moviesService.getLists().then(function (data) {
      vm.lists = data.movie_lists;
    });

    //Call from the pagination to update the page to the selected page
    vm.updateListPage = function (index) {
      options.page = index;

      loadMovies();
    }

    $scope.$watch(function () {
      return vm.selectedList;
    }, function (newValue, oldValue) {
      if (newValue != oldValue) {
        loadMovies();
      }
    });

    function loadMovies() {
      if (vm.selectedList == vm.lists.length) {
        $mdDialog.show({
          controller: 'newListController',
          controllerAs: 'vm',
          templateUrl: 'plugins/movies/components/new-list/new-list.tmpl.html'
        }).then(function (newList) {
          vm.lists.push(newList);
          //TODO: Select newly inserted list
        });
      } else {

        var listId = vm.lists[vm.selectedList].id;

        moviesService.getListMovies(listId, options)
          .then(function (data) {
            vm.movies = data.movies;

            vm.currentPage = data.page;
            vm.totalMovies = data.total_number_of_movies;
            vm.pageSize = data.number_of_movies;
          });
      }
    };


    function showDialog(params) {
      return $mdDialog.show({
        controller: 'seriesUpdateController',
        controllerAs: 'vm',
        templateUrl: 'plugins/series/components/series-update/series-update.tmpl.html',
        locals: {
          showId: vm.show.show_id,
          params: params
        }
      });
    }


    vm.deleteMovie = function (list, movie) {
      var confirm = $mdDialog.confirm()
        .title('Confirm deleting movie from list.')
        .htmlContent("Are you sure you want to delete the movie <b>" + movie.title + "</b> from list <b>" + list.name + "?")
        .ok("Forget")
        .cancel("No");

      $mdDialog.show(confirm).then(function () {
        moviesService.deleteMovie(list.id, movie.id)
          .then(function () {
            var index = vm.movies.indexOf(movie);
            vm.movies.splice(index, 1);
          });
      });
    }

    vm.deleteList = function (list) {
      var confirm = $mdDialog.confirm()
        .title('Confirm deleting movie list.')
        .htmlContent("Are you sure you want to delete the movie list <b>" + list.name + "</b>?")
        .ok("Forget")
        .cancel("No");

      //Actually show the confirmation dialog and place a call to DELETE when confirmed
      $mdDialog.show(confirm).then(function () {
        moviesService.deleteList(list.id)
          .then(function () {
            var index = vm.lists.indexOf(list);
            vm.lists.splice(index, 1);
          });
      });
    }
  }
})();
(function () {
  'use strict';

  var logModule = angular.module('flexget.plugins.log', ['ui.grid', 'ui.grid.autoResize', 'ui.grid.autoScroll']);
  registerPlugin(logModule);

  logModule.run(["$state", "route", "sideNav", "toolBar", function ($state, route, sideNav, toolBar) {
    route.register('log', '/log', 'log-view');
    sideNav.register('/log', 'Log', 'fa fa-file-text-o', 10);
    toolBar.registerButton('Log', 'fa fa-file-text-o', function () {
      $state.go('flexget.log')
    });
  }]);

})();

(function () {
  'use strict';

  logController.$inject = ["$scope"];
  angular
    .module('flexget.plugins.log')
    .component('logView', {
      templateUrl: 'plugins/log/log.tmpl.html',
      controllerAs: 'vm',
      controller: logController
    });

  function logController($scope) {
    var vm = this;

    vm.logStream = false;

    vm.status = 'Connecting';

    vm.filter = {
      lines: 400,
      search: ''
    };

    vm.refreshOpts = {
      debounce: 1000
    };

    vm.toggle = function () {
      if (vm.status == 'Disconnected') {
        vm.refresh();
      } else {
        vm.stop();
      }
    };

    vm.clear = function() {
      vm.gridOptions.data = [];
    };

    vm.stop = function () {
      if (typeof vm.logStream !== 'undefined' && vm.logStream) {
        vm.logStream.abort();
        vm.logStream = false;
        vm.status = "Disconnected";
      }

    };

    vm.refresh = function () {
      // Disconnect existing log streams
      vm.stop();

      vm.status = "Connecting";
      vm.gridOptions.data = [];

      var queryParams = '?lines=' + vm.filter.lines;
      if (vm.filter.search) {
        queryParams = queryParams + '&search=' + vm.filter.search;
      }

      vm.logStream = oboe({url: '/api/server/log/' + queryParams})
        .start(function () {
          $scope.$applyAsync(function () {
            vm.status = "Streaming";
          });
        })
        .node('{message}', function (node) {
          $scope.$applyAsync(function () {
            vm.gridOptions.data.push(node);
          });
        })
        .fail(function (test) {
          $scope.$applyAsync(function () {
            vm.status = "Disconnected";
          });
        })
    };

    var rowTemplate = '<div class="{{ row.entity.log_level | lowercase }}"' +
      'ng-class="{summary: row.entity.message.startsWith(\'Summary\'), accepted: row.entity.message.startsWith(\'ACCEPTED\')}"><div ' +
      'ng-repeat="(colRenderIndex, col) in colContainer.renderedColumns track by col.uid" ' +
      'class="ui-grid-cell" ' +
      'ng-class="{ \'ui-grid-row-header-cell\': col.isRowHeader }"  ui-grid-cell>' +
      '</div></div>';

    vm.gridOptions = {
      data: [],
      enableSorting: true,
      rowHeight: 20,
      columnDefs: [
        {field: 'timestamp', name: 'Time', cellFilter: 'date', enableSorting: true, width: 120},
        {field: 'log_level', name: 'Level', enableSorting: false, width: 65},
        {field: 'plugin', name: 'Plugin', enableSorting: false, width: 80, cellTooltip: true},
        {field: 'task', name: 'Task', enableSorting: false, width: 65, cellTooltip: true},
        {field: 'message', name: 'Message', enableSorting: false, minWidth: 400, cellTooltip: true}
      ],
      rowTemplate: rowTemplate,
      onRegisterApi: function (gridApi) {
        vm.gridApi = gridApi;
        vm.refresh();
      }
    };

    // Cancel timer and stop the stream when navigating away
    $scope.$on("$destroy", function () {
      vm.stop();
    });
  }

})
();

(function () {
    'use strict';

    var historyModule = angular.module("flexget.plugins.history", ['angular.filter']);

    registerPlugin(historyModule);

    historyModule.run(["route", "sideNav", function (route, sideNav) {
        route.register('history', '/history', 'history-view');
        sideNav.register('/history', 'History', 'fa fa-history', 30);
    }]);

})();

(function () {
  'use strict';
  historyController.$inject = ["$http"];
  angular
    .module("flexget.plugins.history")
    .component('historyView', {
      templateUrl: 'plugins/history/history.tmpl.html',
      controllerAs: 'vm',
      controller: historyController,
    });

  function historyController($http) {
    var vm = this;

    vm.title = 'History';
    $http.get('/api/history/')
      .success(function (data) {
        vm.entries = data['entries'];
      })
      .error(function (data, status, headers, config) {
        // log error
      });
  }

})();

(function () {
    'use strict';

    angular.module('flexget.plugins.execute')
        .filter('executePhaseFilter', executePhaseFilter);

    function executePhaseFilter() {
        var phaseDescriptions = {
            input: "Gathering Entries",
            metainfo: "Figuring out meta data",
            filter: "Filtering Entries",
            download: "Downloading Accepted Entries",
            modify: "Modifying Entries",
            output: "Executing Outputs",
            exit: "Finished"
        };

        return function (phase) {
            if (phase in phaseDescriptions) {
                return phaseDescriptions[phase]
            } else {
                return "Processing"
            }
        };
    }

})();
(function () {
    'use strict';

    executeController.$inject = ["$scope", "$interval", "$q", "tasks", "$filter"];
    angular
      .module('flexget.plugins.execute')
        .component('executeView', {
          templateUrl: 'plugins/execute/execute.tmpl.html',
          controllerAs: 'vm',
          controller: executeController,
        });

    function executeController($scope, $interval, $q, tasks, $filter) {
        var vm = this,
            allTasks = [];

        vm.stream = {running: false, tasks: []};
        vm.options = {
            isOpen: false,
            settings: {
                log: true,
                entry_dump: true,
                progress: true,
                summary: true,
                now: true
            },
            optional: [
                {name: 'test', value: false, help: '......', display: 'Test Mode'},
                {name: 'no-cache', value: false, help: 'disable caches. works only in plugins that have explicit support', display: 'Caching'},
                {name: 'stop-waiting', value: null, help: 'matches are not downloaded but will be skipped in the future', display: 'Waiting'},
                {name: 'learn', value: null, help: 'matches are not downloaded but will be skipped in the future', display: 'Learn'},
                {name: 'disable-tracking', value: null, help: 'disable episode advancement for this run', display: 'Tracking'},
                {name: 'discover-now', value: null, help: 'immediately try to discover everything', display: 'Discover'}
            ],
            toggle: function(option) {
                option.value = !option.value;
            }
        };

        // Get a list of tasks for auto complete
        tasks.list()
            .then(function (tasks) {
                allTasks = tasks;
            });

        vm.addTask = function (chip) {
            var chipLower = chip.toLowerCase();

            function alreadyAdded(newChip) {
                for (var i = 0; i < vm.tasksInput.tasks.length; i++) {
                    if (newChip.toLowerCase() == vm.tasksInput.tasks[i].toLowerCase()) {
                        return true
                    }
                }
                return false;
            }

            if (chip.indexOf('*') > -1) {
                for (var i = 0; i < allTasks.length; i++) {
                    var match = new RegExp("^" + chip.replace("*", ".*") + "$", 'i').test(allTasks[i]);
                    if (match && !alreadyAdded(allTasks[i])) {
                        vm.tasksInput.tasks.push(allTasks[i]);
                    }
                }
                return null;
            }

            for (var i = 0; i < allTasks.length; i++) {
                if (chipLower == allTasks[i].toLowerCase() && !alreadyAdded(allTasks[i])) {
                    return chip;
                }
            }
            return null;
        };
        // Used for input form to select tasks to execute
        vm.tasksInput = {
            tasks: [],
            search: [],
            query: function (query) {
                var filter = function () {
                    var lowercaseQuery = angular.lowercase(query);
                    return function filterFn(task) {
                        return (angular.lowercase(task).indexOf(lowercaseQuery) > -1);
                    };
                };
                return query ? allTasks.filter(filter()) : [];
            }
        };

        vm.clear = function () {
            vm.stream.tasks = [];
            vm.stream.running = false;
            vm.options.tasks = [];
        };

        vm.execute = function () {
            vm.stream.running = true;
            vm.stream.tasks = [];

            angular.forEach(vm.tasksInput.tasks, function (task) {
                vm.stream.tasks.push({
                    status: 'pending',
                    name: task,
                    entries: [],
                    percent: 0
                });
            });

            var updateProgress = function () {
                var totalPercent = 0;
                for (var i = 0; i < vm.stream.tasks.length; i++) {
                    totalPercent = totalPercent + vm.stream.tasks[i].percent;
                }
                vm.stream.percent = totalPercent / vm.stream.tasks.length;
            };

            var options = {};
            angular.copy(vm.options.settings, options);
            tasks.execute(vm.tasksInput.tasks, options)
                .log(function(log) {
                    console.log(log);
                })
                .progress(function (update) {
                    var filtered = $filter('filter')(vm.stream.tasks, { status: '!complete' });
                    angular.extend(filtered[0], update);
                    updateProgress();
                })
                .summary(function (update) {
                    var filtered = $filter('filter')(vm.stream.tasks, { status: 'complete' });
                    angular.extend(filtered[filtered.length - 1], update);
                    updateProgress();
                })
                .entry_dump(function (entries) {
                    var filtered = $filter('filter')(vm.stream.tasks, { status: 'complete' });
                    angular.extend(filtered[filtered.length - 1], { entries: entries });
                });
        };

        var getRunning = function () {
            tasks.queue().then(function (tasks) {
                vm.running = tasks
            })
        };
        getRunning();
        var taskInterval = $interval(getRunning, 3000);

        // Cancel timer and stop the stream when navigating away
        $scope.$on("$destroy", function () {
            $interval.cancel(taskInterval);
            if (angular.isDefined(stream)) {
                stream.abort();
            }
        });
    }

})();

(function () {
    'use strict';

    var configModule = angular.module("flexget.plugins.config", ['ui.ace', 'ab-base64', 'angular-cache']);

    registerPlugin(configModule);

    configModule.run(["route", "sideNav", function (route, sideNav) {
        route.register('config', '/config', 'config-view');
        sideNav.register('/config', 'Config', 'fa fa-pencil', 15);
    }]);

})();

(function () {
	'use strict';
	configController.$inject = ["$http", "base64", "$mdDialog", "CacheFactory"];
	angular
		.module("flexget.plugins.config")
		.component('configView', {
			templateUrl: 'plugins/config/config.tmpl.html',
			controllerAs: 'vm',
			controller: configController,
		});

	function configController($http, base64, $mdDialog, CacheFactory) {
		var vm = this;

		if (!CacheFactory.get('aceThemeCache')) {
			CacheFactory('aceThemeCache', {
				storageMode: 'localStorage'
			});
		}

		var aceThemeCache = CacheFactory.get('aceThemeCache');
		
		vm.aceOptions = {
			mode: 'yaml',
			theme: getTheme(),
			onLoad: aceLoaded
		};

		function getTheme() {
			return aceThemeCache.get('theme') ? aceThemeCache.get('theme') : 'chrome';
		}

		function aceLoaded(_editor) {
			_editor.setShowPrintMargin(false);
		}

		vm.updateTheme = function () {
			aceThemeCache.put('theme', vm.aceOptions.theme);
		}

		var themelist = ace.require('ace/ext/themelist');
		vm.themes = themelist.themes;

		$http.get('/api/server/raw_config')
			.then(function (response) {
				var encoded = response.data.raw_config;
				vm.config = base64.decode(encoded);
				vm.origConfig = angular.copy(vm.config);
			}, function (error) {
				// log error
				console.log(error);
			});

		vm.save = function () {
			var encoded = base64.encode(vm.config);
			$http.post('/api/server/raw_config', { raw_config: encoded })
				.then(function (data) {
					var dialog = $mdDialog.alert()
						.title("Update success")
						.ok("Ok")
						.textContent("Your config file has been successfully updated")

					$mdDialog.show(dialog);
					vm.origConfig = angular.copy(vm.config);
				}, function (error) {
					vm.errors = error.data.errors;
				});
		}
	};

})();

(function() {
    'use strict';

    angular
        .module('flexget.directives', [
        ]);
})();
(function () {
    'use strict';

    paletteBackground.$inject = ["flexTheme"];
    angular
        .module('flexget.directives')
        .directive('paletteBackground', paletteBackground);

    /* @ngInject */
    function paletteBackground(flexTheme) {
        var directive = {
            bindToController: true,
            link: link,
            restrict: 'A'
        };
        return directive;

        function link(scope, $element, attrs) {
            var splitColor = attrs.paletteBackground.split(':');
            var color = flexTheme.getPaletteColor(splitColor[0], splitColor[1]);

            if (angular.isDefined(color)) {
                $element.css({
                    'background-color': flexTheme.rgba(color.value),
                    'border-color': flexTheme.rgba(color.value),
                    'color': flexTheme.rgba(color.contrast)
                });
            }
        }
    }
})();
(function() {
  'use strict';

  angular
    .module('flexget.directives')
    .directive('fgMaterialPagination', fgMaterialPagination);

  /* @ngInject */
  function fgMaterialPagination() {
    var directive = {
      restrict: 'E',
      scope: {
        page: '=',
        pageSize: '=',
        total: '=',
        activeClass: '@',
        pagingAction: '&',
      },
      link: pagingLink,
      templateUrl: 'directives/material-pagination/material-pagination.tmpl.html'
    }
    return directive;
  }

  function pagingLink(scope, element, attributes) {
    scope.$watch('[page,total]', function(newValue, oldValue) {
      if(newValue) {
        updateButtons(scope, attributes);
      }
    }, true)
  }

  function addRange(start, end, scope) {
    var i = 0;
    for(i = start; i <= end; i++) {
      scope.stepList.push({
        value: i,
        activeClass: scope.page == i ? scope.activeClass : '',
        action: function() {
          internalAction(scope, this.value);
        }
      })
    }
  }

  function internalAction(scope, page) {
    if(scope.page == page) {
      return;
    }

    scope.pagingAction({
      index: page
    });
  }

  function setPrevNext(scope, pageCount, mode) {
    var disabled, item;
    switch(mode) {
      case 'prev':
        disabled = scope.page - 1 <= 0;
        var prevPage = scope.page - 1 <= 0 ? 1 : scope.page - 1;

        item = {
          value: '<',
          disabled: disabled,
          action: function() {
            if(!disabled) {
              internalAction(scope, prevPage);
            }
          }
        }
        break;

      case 'next':
        disabled = scope.page >= pageCount;
        var nextPage = scope.page + 1 >= pageCount ? pageCount : scope.page + 1;

        item = {
          value: '>',
          disabled: disabled,
          action: function() {
            if(!disabled) {
              internalAction(scope, nextPage);
            }
          }
        }
        break;
    }

    if(item) {
      scope.stepList.push(item);
    }
  }

  function updateButtons(scope) {
    var pageCount = Math.ceil(scope.total / scope.pageSize);

    scope.stepList = [];

    var cutOff = 5;

    // Set left navigator
    setPrevNext(scope, pageCount, 'prev');

    if(pageCount <= cutOff) {
      addRange(1, pageCount, scope);
    } else {
      // Check if page is in the first 3
      // Then we don't have to shift the numbers left, otherwise we get 0 and -1 values
      if(scope.page - 2 < 2) {
        addRange(1, 5, scope);

      // Check if page is in the last 3
      // Then we don't have to shift the numbers right, otherwise we get higher values without any results
      } else if(scope.page + 2 > pageCount) {
        addRange(pageCount - 4, pageCount, scope);

      // If page is not in the start of end
      // Then we add 2 numbers to each side of the current page
      } else {
        addRange(scope.page - 2, scope.page + 2, scope);
      }
    }

    // Set right navigator
    setPrevNext(scope, pageCount, 'next');
  }

})();
(function () {
    'use strict';

    angular
        .module('flexget.components', [
		'flexget.components.requestInterceptor']);

})();

(function () {
    'use strict';

    userConfig.$inject = ["toolBar"];
    angular.module('flexget.components')
        .run(userConfig);

    function userConfig(toolBar) {
        toolBar.registerMenuItem('Manage', 'Profile', 'fa fa-user', function () {
            alert('not implemented yet')
        }, 100);
    }

})();



(function () {
    'use strict';

    angular.module('flexget.components')
        .factory('toolBar', toolbarService);

    function toolbarService() {
        // Add default Manage (cog) menu
        var items = [
            {type: 'menu', label: 'Manage', cssClass: 'fa fa-cog', items: [], width: 2, order: 255}
        ];

        var defaultOrder = 128;

        var getMenu = function (menu) {
            for (var i = 0, len = items.length; i < len; i++) {
                var item = items[i];
                if (item.type == 'menu' && item.label == menu) {
                    return item;
                }
            }
        };

        return {
            items: items,
            registerButton: function (label, cssClass, action, order) {
                if (!order) {
                    order = defaultOrder;
                }
                items.push({type: 'button', label: label, cssClass: cssClass, action: action, order: order});
            },
            registerMenu: function (label, cssClass, width, order) {
                // Ignore if menu already registered
                var existingMenu = getMenu(label);
                if (!existingMenu) {
                    if (!order) {
                        order = defaultOrder;
                    }
                    if (!width) {
                        width = 2;
                    }
                    items.push({type: 'menu', label: label, cssClass: cssClass, items: [], width: 2, order: order});
                }
            },
            registerMenuItem: function (menu, label, cssClass, action, order) {
                if (!order) {
                    order = defaultOrder;
                }

                menu = getMenu(menu);
                if (menu) {
                    menu.items.push({label: label, cssClass: cssClass, action: action, order: order});
                } else {
                    throw 'Unable to register menu item ' + label + ' as Menu ' + menu + ' was not found';
                }
            }
        }
    }

})();



(function () {
    'use strict';

    toolbarDirective.$inject = ["toolBar"];
    angular.module('flexget.components')
        .directive('toolBar', toolbarDirective);

    function toolbarDirective(toolBar) {
        return {
            restrict: 'E',
            scope: {},
            templateUrl: 'components/toolbar/toolbar.tmpl.html',
            controllerAs: 'vm',
            controller: ["sideNav", function (sideNav) {
                var vm = this;
                vm.toggle = sideNav.toggle;
                vm.toolBarItems = toolBar.items;
            }]
        };
    }

})();
(function () {
    'use strict';

    sideNavService.$inject = ["$rootScope", "$mdSidenav", "$mdMedia"];
    angular.module('flexget.components')
        .factory('sideNav', sideNavService);

    function sideNavService($rootScope, $mdSidenav, $mdMedia) {
        var items = [];

        var toggle = function () {
            if ($mdSidenav('left').isLockedOpen()) {
                $rootScope.menuMini = !$rootScope.menuMini;
            } else {
                $rootScope.menuMini = false;
                $mdSidenav('left').toggle();
            }
        };

        var close = function () {
            if (!$mdMedia('gt-lg')) {
                $mdSidenav('left').close();
            }
        };

        return {
            toggle: toggle,
            close: close,
            register: function (href, caption, icon, order) {
                href = '#' + href;
                items.push({href: href, caption: caption, icon: icon, order: order})
            },
            items: items
        }
    }

})();



(function () {
    'use strict';

    angular.module('flexget.components')
        .directive('sideNav', sideNavDirective);

    function sideNavDirective() {
        return {
            restrict: 'E',
            replace: 'true',
            templateUrl: 'components/sidenav/sidenav.tmpl.html',
            controllerAs: 'vm',
            controller: ["$mdMedia", "sideNav", function ($mdMedia, sideNav) {
                var vm = this;
                vm.toggle = sideNav.toggle;
                vm.navItems = sideNav.items;
                vm.close = sideNav.close;
            }]
        }
    }

})
();
(function () {
    'use strict';

    angular
        .module("flexget.components.requestInterceptor", []);
})();
(function() {
  'use strict';

  urlInterceptor.$inject = ["$q", "$log"];
  angular
	  .module('flexget.components.requestInterceptor')
	  .factory('urlInterceptor', urlInterceptor)
	  .config(["$httpProvider", function ($httpProvider) {
		  $httpProvider.interceptors.push('urlInterceptor')
	  }]);

  function urlInterceptor($q, $log) {
    var service = {
      request: request
    };
    return service;

    function request(config) {
		if (config.url.startsWith('/api/') && !config.url.endsWith('/')) {
			config.url += '/';
		}
		return config;
    }
  }
})();

(function () {
    'use strict';

    var home = angular.module("flexget.home", ['angular.filter']);
    registerPlugin(home);

    home.run(["route", function (route) {
        route.register('home', '/home', 'home');
    }]);
})();

(function () {

  angular
    .module('flexget.home')
    .component('home', {
      templateUrl: 'components/home/home.tmpl.html'
    })
})();

(function () {
    'use strict';

    errorService.$inject = ["$mdToast", "$mdDialog"];
    angular.module('flexget.components')
        .factory('errorService', errorService);

    function errorService($mdToast, $mdDialog) {
        return {
            showToast: function(error) {
                 var toast = {
                    templateUrl: 'components/error/toast.tmpl.html',
                    position: 'bottom right',
                    controller: toastController,
                    controllerAs: 'vm',
                    locals: {
                        error: error
                    }
                }

                $mdToast.show(toast);
            }
        }

        function dialogController(error) {
            var vm = this;

            vm.error = error;

            vm.close = function() {
                $mdDialog.hide();
            }
        }

        function toastController(error) {
            var vm = this;

            var dialog = {
                templateUrl: 'components/error/dialog.tmpl.html',
                controller: dialogController,
                controllerAs: 'vm',
                locals: {
                    error: error
                }
            }

            vm.text = "Damnit Flexget, you had one job!";

            vm.openDetails = function() {
                $mdDialog.show(dialog);
            }
        };
    }

})();
(function () {
    'use strict';

    authService.$inject = ["$state", "$http", "$q"];
    angular.module('flexget.components')
        .factory('authService', authService);

    function authService($state, $http, $q) {
        var loggedIn, prevState, prevParams;

        loggedIn = false;

        return {
            loggedIn: function () {
                var def = $q.defer();

                if (loggedIn) {
                    def.resolve(loggedIn);
                } else {
                    $http.get("/api/server/version/")
                        .success(function () {
                            def.resolve();
                        })
                        .error(function (data) {
                            def.reject()
                        })
                }

                return def.promise;
            },
            login: function (username, password, remember) {
                if (!remember) {
                    remember = false;
                }

                return $http.post('/api/auth/login/', {username: username, password: password}, { params: { remember: remember } })
                    .success(function () {
                        loggedIn = true;

                        if (prevState) {
                            $state.go(prevState, prevParams);
                        } else {
                            $state.go('flexget.home');
                        }

                    })
            },
            state: function (state, params) {
                if (state.name != 'login') {
                    prevState = state;
                    prevParams = params;
                }
            }
        }
    }

})();
(function () {
    'use strict';

    loginController.$inject = ["$stateParams", "authService"];
    angular.module('flexget.components')
        .controller('LoginController', loginController);

    function loginController($stateParams, authService) {
        var vm = this;

        vm.timeout = $stateParams.timeout;
        vm.remember = false;
        vm.error = '';
        vm.credentials = {
            username: '',
            password: ''
        };

        vm.login = function () {
            authService.login(vm.credentials.username, vm.credentials.password, vm.remember)
                .error(function (data) {
                    vm.credentials.password = '';
                    if ('message' in data) {
                        vm.error = data.message;
                    } else {
                        vm.error = 'Error during authentication';
                    }
                });
        };
    }

})();
(function () {
  'use strict';

  authenticationSetup.$inject = ["$rootScope", "$state", "$http", "toolBar", "authService"];
  authenticationConfig.$inject = ["$httpProvider", "$stateProvider"];
  angular.module('flexget.components')
  .run(authenticationSetup)
  .config(authenticationConfig);

  function authenticationSetup($rootScope, $state, $http, toolBar, authService) {
    var loginEvent = $rootScope.$on('event:auth-loginRequired', function (event, timeout) {
      $state.go('login', { timeout: timeout });
    });

    var logout = function () {
      $http.get('/api/auth/logout/')
      .success(function () {
        $state.go('login');
      });
    };

    /* Ensure user is authenticated when changing states (pages) unless we are on the login page */
    var authenticated = $rootScope.$on('$stateChangeStart', function (event, toState, toParams) {
      if (toState.name === 'login') {
        return;
      }

      authService.loggedIn()
      .then(function (loggedIn) {
        // already logged in
      }, function () {
        // Not logged in
        event.preventDefault();
        authService.state(toState, toParams);
        $rootScope.$broadcast('event:auth-loginRequired', false);
      });
    });

    toolBar.registerMenuItem('Manage', 'Logout', 'fa fa-sign-out', logout, 255);
  }

  function authenticationConfig($httpProvider, $stateProvider) {
    /* Register login page and redirect to page when login is required */
    $stateProvider.state('login', {
      controller: 'LoginController',
      controllerAs: 'vm',
      templateUrl: 'components/authentication/login.tmpl.html',
    });


    /* Intercept 401/403 http return codes and redirect to login page */

    $httpProvider
    .interceptors.push(['$rootScope', '$q', '$injector', function ($rootScope, $q, $injector) {
      var loginRequired = function () {
        var stateService = $injector.get('$state');
        var authService = $injector.get('authService');
        authService.state(stateService.current, stateService.params);
        $rootScope.$broadcast('event:auth-loginRequired', true);
      };

      return {
        responseError: function (rejection) {
          if (!rejection.config.ignoreAuthModule) {
            switch (rejection.status) {
              case 401:
              case 403:
                loginRequired();
                break;
            }
          }
          // otherwise, default behaviour
          return $q.reject(rejection);
        },
      };
    }]);
  }
})();

(function () {
    'use strict';

    tasksService.$inject = ["$rootScope", "$http", "$q"];
    angular.module('flexget.components')
        .service('tasks', tasksService);

    function tasksService($rootScope, $http, $q) {
        // List tasks
        this.list = function () {
            return $http.get('/api/tasks/')
                .then(
                    function (response) {
                        var tasks = [];
                        angular.forEach(response.data.tasks, function (task) {
                            this.push(task.name);
                        }, tasks);
                        return tasks
                    },
                    function (httpError) {
                        throw httpError.status + " : " + httpError.data;
                    });
        };

        // Execute task(s), return stream log etc
        this.execute = function (task_names, options) {
            var deferred = $q.defer();

            console.log(options);

            options.tasks = task_names;
            var on = function (event, pattern, callback) {
                var wrappedCallback = function () {
                    var args = arguments;

                    return $rootScope.$evalAsync(function () {
                        return callback.apply(stream, args);
                    });
                };

                if (pattern) {
                    stream.on(event, pattern, wrappedCallback);
                } else {
                    stream.on(event, wrappedCallback)
                }
            };

            var stream = oboe({
                url: '/api/tasks/execute/',
                body: options,
                method: 'POST'
            }).done(function () {
                deferred.resolve("finished stream");
            }).fail(function (error) {
                deferred.reject(error)
            });

            deferred.promise.log = function (callback) {
                on('node', 'log', callback);
                return deferred.promise;
            };

            deferred.promise.progress = function (callback) {
                on('node', 'progress', callback);
                return deferred.promise;
            };

            deferred.promise.summary = function (callback) {
                on('node', 'summary', callback);
                return deferred.promise;
            };

            deferred.promise.entry_dump = function (callback) {
                on('node', 'entry_dump', callback);
                return deferred.promise;
            };

            deferred.promise.abort = function () {
                return stream.abort();
            };

            return deferred.promise;
        };

        this.queue = function () {
            var defer = $q.defer();

            $http.get('/api/tasks/queue/', {ignoreLoadingBar: true}).then(function (response) {
                defer.resolve(response.data.tasks);
            }, function (response) {
                defer.reject(response);
            });

            return defer.promise;
        };

        // Update task config
        this.update = function () {

        };

        // add task
        this.add = function () {

        };

        // Delete task
        this.delete = function () {

        }
    }
})();
(function () {
    'use strict';
    
    schemaService.$inject = ["$http"];
    angular.module('flexget.services')
        .service('schema', schemaService);
    
    function schemaService($http) {
        this.get = function (path) {
            // TODO: Add cache?
           
            if (!path.endsWith('/')) {
                path = path + '/';
            }
            return $http.get('/api/schema/' + path)
                .then(
                    function (response) {
                        return response.data
                    },
                    function (httpError) {
                        throw httpError.status + " : " + httpError.data;
                    });
        };
        
        this.config = function (name) {
            return this.get('config/' + name)
        };

        this.plugin = function (name) {
            return this.get('config/' + name)
        };
    }
    
})();



(function () {
    'use strict';

    angular
        .module('flexget.plugins', []);

})();
(function () {
  'use strict';

  themesConfig.$inject = ["$mdThemingProvider"];
  flexTheme.$inject = ["$mdThemingProvider"];
  angular
  .module('flexget')
  .config(themesConfig)
  .provider('flexTheme', flexTheme);

  function themesConfig($mdThemingProvider) {
    $mdThemingProvider.theme('default')
    .primaryPalette('orange', {
      default: '800'
    })
    .accentPalette('deep-orange', {
      default: '500'
    })
    .warnPalette('amber');
  }

  function flexTheme($mdThemingProvider) {
    return {
      $get: function () {
        return {
          getPaletteColor: function (paletteName, hue) {
            if (
              angular.isDefined($mdThemingProvider._PALETTES[paletteName])
              && angular.isDefined($mdThemingProvider._PALETTES[paletteName][hue])
            ) {
              return $mdThemingProvider._PALETTES[paletteName][hue];
            }
          },
          rgba: $mdThemingProvider._rgba,
          palettes: $mdThemingProvider._PALETTES,
          themes: $mdThemingProvider._THEMES,
          parseRules: $mdThemingProvider._parseRules,
        };
      },
    };
  }
})();

(function () {
  'use strict';

  routeService.$inject = ["$stateProvider"];
  routeConfig.$inject = ["$stateProvider", "$urlRouterProvider"];
  angular.module('flexget')
    .provider('route', routeService)
    .config(routeConfig);

  function routeService($stateProvider) {
    this.$get = function () {
      return {
        register: function (name, url, template) {
          $stateProvider.state('flexget.' + name, {
            url: url,
            template: '<' + template + ' flex layout="row"></' + template + '/>'
          });
        }
      };
    };
  }

  function routeConfig($stateProvider, $urlRouterProvider) {
    $stateProvider
    // 404 & 500 pages
      .state('404', {
        url: '/404',
        templateUrl: '404.tmpl.html',
        controllerAs: 'vm',
        controller: ["$state", function ($state) {
          var vm = this;
          vm.goHome = function () {
            $state.go('flexget.home');
          };
        }]
      })

      .state('flexget', {
        abstract: true,
        templateUrl: 'layout.tmpl.html'
      });

    // set default routes when no path specified
    $urlRouterProvider.when('', '/home');
    $urlRouterProvider.when('/', '/home');

    // always goto 404 if route not found
    $urlRouterProvider.otherwise('/404');

  }
})();

angular.module("flexget").run(["$templateCache", function($templateCache) {$templateCache.put("404.tmpl.html","<div class=\"login\" layout=\"column\" layout-align=\"center\"><div class=\"header\"></div><div layout=\"row\" layout-align=\"center stretch\"><md-card flex-xs=\"100\" flex-sm=\"70\" flex-md=\"50\" flex-gt-md=\"30\" layout-padding=\"\"><md-card-content class=\"text-center\"><h1 class=\"md-display-1\">Uh oh! 404 Error</h1><p>Look like the page you requested was not found</p><md-button class=\"md-primary md-raised\" ng-click=\"vm.goHome()\">Go Home</md-button></md-card-content></md-card></div></div>");
$templateCache.put("construction.tmpl.html","<div layout=\"column\" flex=\"\" layout-align=\"center center\" layout-fill=\"\"><div layout=\"row\" flex=\"\" layout-padding=\"\" layout-align=\"center center\"><md-icon md-font-icon=\"fa-code\" class=\"fa construction-icon md-icon\" layout-fill=\"\"></md-icon></div><div layout=\"row\" flex=\"\"><div layout=\"column\" flex=\"\" layout-align=\"center center\"><div layout=\"row\" flex=\"\" layout-align=\"center center\"><span class=\"md-headline\">Even though some parts of this page may seem to work, it\'s not completely done yet.</span></div><div layout=\"row\" flex=\"\"><span class=\"md-subhead\">We are working hard to make this page usable soon.</span></div><div layout=\"row\" flex=\"\"><span class=\"md-subhead\">Check back in a few versions to see if this page already works.</span></div></div></div></div>");
$templateCache.put("layout.tmpl.html","<div class=\"header md-whiteframe-4dp\" ng-class=\"menuMini ? \'header-mini\': \'header-full\'\"><div class=\"logo\"><a href=\"#/home\"></a></div><tool-bar></tool-bar></div><div layout=\"row\" flex=\"\" ng-class=\"menuMini ? \'nav-menu-mini\': \'nav-menu-full\'\"><side-nav></side-nav><md-content ui-view=\"\" layout-fill=\"\" flex=\"\" layout=\"column\" id=\"content\"></md-content></div>");
$templateCache.put("components/authentication/login.tmpl.html","<div class=\"login\" layout=\"column\" flex=\"\" layout-align=\"start stretch\"><div class=\"header\"></div><form name=\"loginForm\"><div layout=\"row\" layout-align=\"center stretch\"><md-card flex-xs=\"100\" flex-sm=\"70\" flex-md=\"50\" flex-gt-md=\"30\" layout-padding=\"\"><p style=\"color: orange\" class=\"text-success text-center\" ng-if=\"vm.timeout == \'true\'\">Your session timed out</p><p style=\"color: red\" class=\"text-center\">{{ vm.error }}</p><md-input-container class=\"md-block\"><label>Username</label> <input id=\"username\" ng-model=\"vm.credentials.username\"></md-input-container><md-input-container class=\"md-block\"><label>Password</label> <input id=\"password\" ng-model=\"vm.credentials.password\" type=\"password\"></md-input-container><div layout=\"column\" layout-align=\"center center\"><md-checkbox md-no-ink=\"\" aria-label=\"Remember Me\" ng-model=\"vm.remember\" class=\"md-primary\">Remember Me</md-checkbox></div><md-button type=\"submit\" class=\"md-raised md-primary\" data-ng-click=\"vm.login()\">Login</md-button></md-card></div></form></div>");
$templateCache.put("components/error/dialog.tmpl.html","<md-dialog aria-label=\"Error Details\" ng-cloak=\"\"><md-dialog-content><div class=\"md-dialog-content\"><h1>TODO: Add error data</h1><h2>TODO: Check if copy to clipboard is useful, as well as link the open new issue on github</h2><pre>{{ vm.error | json }}</pre></div></md-dialog-content><md-dialog-actions layout=\"row\"><md-button ng-click=\"vm.close()\">Close</md-button></md-dialog-actions></md-dialog>");
$templateCache.put("components/error/toast.tmpl.html","<md-toast><span class=\"md-toast-text\" flex=\"\">{{ vm.text }}</span><md-button class=\"md-highlight\" ng-click=\"vm.openDetails()\">Details</md-button></md-toast>");
$templateCache.put("components/home/home.tmpl.html","<md-content layout-xs=\"column\" layout=\"row\" flex=\"\"><div layout=\"column\" flex=\"\" flex-gt-sm=\"50\" flex-offset-gt-sm=\"25\"><md-card><md-card-header palette-background=\"orange:600\"><md-card-header-text><span class=\"md-title\">Flexget Web Interface</span> <span class=\"md-subhead\">Under Development</span></md-card-header-text></md-card-header><md-card-content><p><b>We need your help! If you are an AngularJS developer or can help with the layout/design/css then please join in the effort!</b></p><p>The interface is not yet ready for end users. Consider this preview only state.</p><p>If you still use it anyways, please do report back to us how well it works, issues, ideas etc..</p><p>There is a functional API with documentation available at <a href=\"/api\">/api</a></p><p>More information: <a href=\"http://flexget.com/wiki/Web-UI\" target=\"_blank\">http://flexget.com/wiki/Web-UI</a></p><p>Gitter Chat: <a href=\"https://gitter.im/Flexget/Flexget\" target=\"_blank\">https://gitter.im/Flexget/Flexget</a></p><div layout=\"row\" layout-align=\"center center\"><md-button class=\"md-icon-button\" aria-label=\"GitHub\" href=\"http://github.com/Flexget/Flexget\" target=\"_blank\"><md-icon class=\"md-icon fa fa-github md-headline\"></md-icon><md-tooltip>GitHub</md-tooltip></md-button><md-button class=\"md-icon-button\" aria-label=\"Flexget.com\" href=\"http://flexget.com\" target=\"_blank\"><md-icon class=\"md-icon fa fa-home md-headline\"></md-icon><md-tooltip>Wiki</md-tooltip></md-button><md-button class=\"md-icon-button\" aria-label=\"Flexget.com\" href=\"https://gitter.im/Flexget/Flexget\" target=\"_blank\"><md-icon class=\"md-icon fa fa-comment md-headline\"></md-icon><md-tooltip>Chat</md-tooltip></md-button><md-button class=\"md-icon-button\" aria-label=\"Forum\" href=\"http://discuss.flexget.com/\" target=\"_blank\"><md-icon class=\"md-icon fa fa-forumbee md-headline\"></md-icon><md-tooltip>Forum</md-tooltip></md-button></div></md-card-content></md-card></div></md-content>");
$templateCache.put("components/sidenav/sidenav.tmpl.html","<md-sidenav layout=\"column\" class=\"nav-menu md-sidenav-left md-sidenav-left md-whiteframe-z2\" md-component-id=\"left\" md-is-locked-open=\"$mdMedia(\'gt-sm\')\"><md-content layout=\"column\" flex=\"\"><md-list><md-list-item ng-repeat=\"item in ::vm.navItems | orderBy : \'order\'\"><md-button href=\"{{ ::item.href }}\" ng-click=\"vm.close()\" flex=\"\"><md-icon class=\"{{ ::item.icon }}\"></md-icon>{{ ::item.caption }}</md-button></md-list-item></md-list></md-content></md-sidenav>");
$templateCache.put("components/toolbar/toolbar.tmpl.html","<div class=\"admin-toolbar\"><md-toolbar class=\"admin-toolbar\"><div class=\"md-toolbar-tools\"><md-button class=\"md-icon-button\" ng-click=\"vm.toggle()\" style=\"width: 40px\"><md-icon class=\"fa fa-bars\" aria-label=\"Menu\"></md-icon></md-button><span flex=\"\"></span><div ng-repeat=\"item in ::vm.toolBarItems | orderBy:\'order\'\"><md-button aria-label=\"{{ item.label }}\" class=\"md-icon-button\" ng-click=\"item.action()\" ng-if=\"::item.type == \'button\'\"><md-tooltip>{{ ::item.label }}</md-tooltip><md-icon md-menu-origin=\"\" class=\"{{ ::item.cssClass }}\"></md-icon></md-button><md-menu ng-if=\"::item.type == \'menu\'\"><md-button aria-label=\"{{ ::item.label }}\" class=\"md-icon-button\" ng-click=\"$mdOpenMenu($event)\"><md-tooltip>{{ ::item.label }}</md-tooltip><md-icon md-menu-origin=\"\" class=\"{{ ::item.cssClass }}\"></md-icon></md-button><md-menu-content width=\"{{ ::item.width }}\"><md-menu-item ng-repeat=\"menuItem in ::item.items | orderBy:\'order\'\"><md-button ng-click=\"menuItem.action()\"><md-icon md-menu-origin=\"\" class=\"{{ ::menuItem.cssClass }}\"></md-icon>{{ ::menuItem.label }}</md-button></md-menu-item></md-menu-content></md-menu></div></div></md-toolbar></div>");
$templateCache.put("directives/material-pagination/material-pagination.tmpl.html","<div layout=\"row\" class=\"fg-material-paging\" layout-align=\"center center\"><md-button class=\"md-raised fg-pagination-button\" ng-repeat=\"step in stepList\" ng-click=\"step.action()\" ng-class=\"step.activeClass\" ng-disabled=\"step.disabled\">{{ step.value }}</md-button></div>");
$templateCache.put("plugins/config/config.tmpl.html","<md-content layout=\"column\" flex=\"\" layout-fill=\"\"><md-toolbar class=\"md-warn\"><p class=\"md-toolbar-tools\"><span>This page is still pretty much in beta. Please take a backup before trying to save a new config.</span></p></md-toolbar><div layout=\"row\" layout-padding=\"\"><div layout=\"row\" flex=\"\"><div layout=\"column\" flex=\"25\" layout-align=\"center start\"><md-button class=\"md-raised md-primary\" ng-click=\"vm.save()\" ng-disabled=\"vm.config == vm.origConfig\">Save and apply</md-button></div></div><div layout=\"column\" flex=\"30\"><md-input-container class=\"md-block\"><label>Theme</label><md-select ng-model=\"vm.aceOptions.theme\" ng-change=\"vm.updateTheme()\"><md-option ng-repeat=\"theme in vm.themes\" value=\"{{ theme.name }}\">{{ theme.caption }}</md-option></md-select></md-input-container></div></div><div layout=\"row\" ng-if=\"vm.errors\"><md-list flex=\"\"><md-list-item class=\"md-2-line\" ng-repeat=\"error in vm.errors\"><div class=\"md-list-item-text\"><h3><b>Path:</b> {{ error.config_path }}</h3><h4><b>Message:</b> {{ error.error }}</h4></div><md-divider ng-if=\"!$last\"></md-divider></md-list-item></md-list></div><div layout=\"row\" flex=\"\"><div ui-ace=\"vm.aceOptions\" flex=\"\" ng-model=\"vm.config\"></div></div></md-content>");
$templateCache.put("plugins/execute/execute.tmpl.html","<md-content layout=\"column\" layout-fill=\"\" flex=\"\" class=\"execute\" ng-hide=\"vm.stream.tasks.length\"><execute-input options=\"vm.options\" running=\"vm.running\" execute=\"vm.execute\" tasks-input=\"vm.tasksInput\" add-task=\"vm.addTask\"></execute-input></md-content><md-content layout=\"column\" layout-fill=\"\" flex=\"\" ng-show=\"vm.stream.tasks.length\"><execute-stream stream=\"vm.stream\" running=\"vm.running\" clear=\"vm.clear\"></execute-stream></md-content>");
$templateCache.put("plugins/history/history.tmpl.html","<md-content flex=\"\" layout-fill=\"\"><section ng-repeat=\"(key, value) in vm.entries | groupBy: \'time | limitTo : 10\'\"><md-subheader class=\"md-primary\">{{ key }}</md-subheader><md-list layout-padding=\"\"><md-list-item class=\"md-2-line\" ng-repeat=\"entry in value\"><div class=\"md-list-item-text\"><h3>{{ entry.title }}</h3><p>{{ entry.task }}</p></div></md-list-item></md-list></section></md-content>");
$templateCache.put("plugins/log/log.tmpl.html","<md-card class=\"log\" flex=\"\" layout=\"column\" layout-fill=\"\"><md-card-header><md-card-header-text><span class=\"md-title\">Server log</span> <span class=\"md-subhead\">{{ vm.status }}</span></md-card-header-text><md-icon class=\"fa fa-filter\"></md-icon><md-input-container class=\"md-block\" style=\"margin: 0px\" flex=\"60\" flex-gt-md=\"70\"><label>Filter</label> <input type=\"text\" aria-label=\"message\" ng-model=\"vm.filter.search\" ng-change=\"vm.refresh()\" ng-model-options=\"vm.refreshOpts\"><div class=\"hint\">Supports operators and, or, (), and \"str\"</div></md-input-container><md-menu><md-button class=\"widget-button md-icon-button\" ng-click=\"$mdOpenMenu()\" aria-label=\"open menu\"><md-icon md-font-icon=\"fa fa-ellipsis-v\"></md-icon></md-button><md-menu-content><md-menu-item layout-margin=\"\"><md-input-container><label>Max Lines</label> <input type=\"number\" aria-label=\"lines\" ng-model=\"vm.filter.lines\" ng-change=\"vm.refresh()\" ng-model-options=\"vm.refreshOpts\"></md-input-container></md-menu-item><md-menu-item><md-button ng-click=\"vm.clear()\"><md-icon class=\"fa fa-eraser\" ng-class=\"\"></md-icon>Clear</md-button></md-menu-item><md-menu-item><md-button ng-click=\"vm.toggle()\"><md-icon class=\"fa\" ng-class=\"vm.logStream ? \'fa fa-stop\' : \'fa fa-play\'\"></md-icon>{{ vm.logStream ? \'Stop\' : \'Start\' }}</md-button></md-menu-item></md-menu-content></md-menu></md-card-header><div layout=\"row\" flex=\"\" layout-margin=\"\"><div flex=\"\" id=\"log-grid\" ui-grid=\"vm.gridOptions\" ui-grid-auto-resize=\"\" ui-grid-auto-scroll=\"\"></div></div></md-card>");
$templateCache.put("plugins/movies/movies.tmpl.html","<div layout=\"column\" flex=\"\"><md-content flex=\"\" layout-fill=\"\" ng-if=\"vm.lists\"><md-tabs md-dynamic-height=\"\" md-border-bottom=\"\" md-selected=\"vm.selectedList\"><md-tab ng-repeat=\"list in vm.lists\"><md-tab-label layout-fill=\"\"><section layout=\"row\" layout-align=\"center center\" layout-fill=\"\"><span>{{ ::list.name }}</span> <a href=\"\"><md-icon md-font-icon=\"fa-trash-o\" class=\"fa tab-icon fa-lg\" ng-click=\"vm.deleteList(list)\"></md-icon></a></section></md-tab-label><md-tab-body><md-content layout=\"row\" layout-wrap=\"\" layout-padding=\"\"><movie-entry flex=\"100\" flex-gt-md=\"50\" flex-gt-lg=\"33\" movie=\"::movie\" delete-movie=\"vm.deleteMovie(list, movie)\" ng-repeat=\"movie in vm.movies\" class=\"animate-remove\"></movie-entry></md-content></md-tab-body></md-tab><md-tab><md-tab-label><md-icon md-font-icon=\"fa-plus-circle\" class=\"fa tab-icon-plus fa-lg\"></md-icon></md-tab-label></md-tab></md-tabs></md-content><fg-material-pagination page=\"vm.currentPage\" page-size=\"vm.pageSize\" total=\"vm.totalMovies\" active-class=\"md-primary\" paging-action=\"vm.updateListPage(index)\"></fg-material-pagination></div>");
$templateCache.put("plugins/schedule/schedule.tmpl.html","<div layout=\"column\" flex=\"\"><ng-include src=\"\'construction.tmpl.html\'\" layout=\"row\"></ng-include><div layout=\"row\"><pre>{{ vm.models | json }}</pre><div ng-repeat=\"model in vm.models\"><div class=\"col-xs-3\"><form name=\"myForm\" sf-schema=\"vm.schema\" sf-form=\"vm.form\" sf-model=\"vm.model\" ng-submit=\"onSubmit(myForm)\"></form></div></div></div></div>");
$templateCache.put("plugins/seen/seen.tmpl.html","<div layout=\"column\" flex=\"\"><seen-entry ng-repeat=\"entry in ::vm.entries\" entry=\"entry\"></seen-entry></div>");
$templateCache.put("plugins/series/series-episodes.tmpl.html","<md-card layout=\"column\" layout-wrap=\"\" layout-fill=\"\" class=\"episodes-list-card\"><md-card-content ng-style=\"{\'background-image\':\'url({{vm.show.metadata.banner}})\'}\"><div class=\"episodes-backdrop-image-shadow\"></div><ng-transclude></ng-transclude><div class=\"episodes-list\"><series-episode episode=\"episode\" delete-episode=\"vm.deleteEpisode(episode)\" show=\"vm.show\" reset-releases=\"vm.resetReleases(episode)\" ng-repeat=\"episode in vm.show.episodes\"></series-episode></div><fg-material-pagination page=\"vm.currentPage\" page-size=\"vm.pageSize\" total=\"vm.show.totalEpisodes\" active-class=\"md-primary\" paging-action=\"vm.updateListPage(index)\"></fg-material-pagination></md-card-content></md-card>");
$templateCache.put("plugins/series/series.tmpl.html","<div layout=\"column\" flex=\"\"><md-toolbar class=\"md-warn\"><span class=\"md-toolbar-tools\" flex=\"\">Please note that performed operations on this page might not be persistent. Depending on your config, settings might get overriden and data might be recreated.</span></md-toolbar><md-input-container><label>Search</label> <input ng-model=\"vm.searchTerm\" ng-change=\"vm.search()\" ng-model-options=\"{ debounce: 1000 }\"></md-input-container><md-content layout=\"row\" layout-wrap=\"\" layout-padding=\"\"><series-show show=\"show\" forget-show=\"vm.forgetShow(show)\" layout=\"row\" flex=\"100\" flex-gt-md=\"50\" flex-gt-lg=\"33\" ng-repeat-start=\"show in vm.series\"><md-button class=\"md-primary md-raised\" ng-click=\"vm.showEpisodes(show)\">Episodes</md-button><span class=\"show-indicator\" ng-if=\"show == vm.selectedShow\"></span></series-show><series-episodes-view ng-repeat-end=\"\" ng-if=\"vm.areEpisodesOnShowRow(vm.selectedShow, $index)\" show=\"vm.selectedShow\" class=\"series-episodes\"><md-button class=\"md-fab md-mini hide-episodes-button\" ng-click=\"vm.hideEpisodes()\" aria-label=\"hide the episodes\"><i class=\"fa fa-times\" aria-hidden=\"true\"></i></md-button></series-episodes-view></md-content><fg-material-pagination page=\"vm.currentPage\" page-size=\"vm.pageSize\" total=\"vm.totalShows\" active-class=\"md-primary\" paging-action=\"vm.updateListPage(index)\"></fg-material-pagination></div>");
$templateCache.put("services/modal/modal.dialog.circular.tmpl.html","<md-dialog><md-dialog-content><h2>{{ vm.title }}</h2><div layout=\"row\" layout-align=\"center center\"><p ng-if=\"content\">{{ vm.content }}</p><md-progress-circular ng-if=\"vm.showCircular\" md-diameter=\"30\" class=\"md-primary\" md-mode=\"indeterminate\"></md-progress-circular></div></md-dialog-content><md-dialog-actions ng-if=\"vm.ok || vm.cancel\"><md-button ng-if=\"vm.cancel\" ng-click=\"vm.abort()\" class=\"md-primary\">{{ vm.cancel }}</md-button><md-button ng-if=\"vm.ok\" ng-click=\"vm.hide()\" class=\"md-primary\">{{ vm.ok }}</md-button></md-dialog-actions></md-dialog>");
$templateCache.put("services/modal/modal.tmpl.html","<div class=\"modal-header\"><h3>{{ modalOptions.headerText }}</h3></div><div class=\"modal-body\"><p>{{ modalOptions.bodyText }}</p></div><div class=\"modal-footer\"><button ng-if=\"modalOptions.okText\" type=\"button\" class=\"btn btn-{{ modalOptions.okType }}\" data-ng-click=\"ok()\">{{ modalOptions.okText }}</button> <button ng-if=\"modalOptions.closeText\" type=\"button\" class=\"btn btn-{{ modalOptions.closeType }}\" data-ng-click=\"close()\">{{ modalOptions.closeText }}</button></div>");
$templateCache.put("plugins/execute/components/execute-input/execute-input.tmpl.html","<div layout=\"row\" layout-align=\"center center\"><md-card flex=\"\" flex-gt-sm=\"50\" flex-gt-md=\"40\" class=\"task-search\"><md-card-header><md-card-header-text flex=\"\"><span class=\"md-title\">{{ vm.running.length }} Tasks in Queue</span> <span class=\"md-subhead\" ng-if=\"vm.running[0]\">{{ vm.running[0].name }} ({{ vm.running[0].current_phase }})</span></md-card-header-text><md-menu><md-button class=\"widget-button md-icon-button\" ng-click=\"$mdOpenMenu()\" aria-label=\"open menu\"><md-icon md-font-icon=\"fa fa-ellipsis-v\"></md-icon></md-button><md-menu-content width=\"3\"><md-menu-item ng-repeat=\"option in vm.options.optional\"><md-button ng-click=\"vm.options.toggle(option)\"><md-tooltip>{{ option.help }}</md-tooltip><md-icon ng-class=\"option.value ? \'fa fa-ban\' : \'fa fa-check\'\"></md-icon>{{ option.display }}</md-button></md-menu-item></md-menu-content></md-menu></md-card-header><md-card-content><md-chips ng-model=\"vm.tasksInput.tasks\" md-autocomplete-snap=\"\" md-require-match=\"false\" md-transform-chip=\"vm.addTask($chip)\"><md-autocomplete md-items=\"task in vm.tasksInput.query(vm.tasksInput.search)\" md-item-text=\"task\" placeholder=\"Enter task(s) to execute\" md-selected-item=\"selectedItem\" md-search-text=\"vm.tasksInput.search\"><span md-highlight-text=\"vm.tasksInput.search\">{{ task }}</span></md-autocomplete></md-chips><div flex=\"\"></div><div layout=\"row\" layout-align=\"center center\"><div flex=\"100\" flex-gt-md=\"50\" layout=\"column\"><md-button class=\"md-raised md-primary\" ng-click=\"vm.execute()\">Execute</md-button></div></div></md-card-content></md-card></div>");
$templateCache.put("plugins/execute/components/execute-stream/execute-stream.tmpl.html","<div><div><md-progress-linear md-mode=\"determinate\" value=\"{{ vm.stream.percent }}\"></md-progress-linear></div><span class=\"md-subhead\" ng-if=\"vm.running[0]\">{{ vm.running[0].name }} ({{ vm.running[0].current_phase }})</span><md-tabs md-selected=\"selectedIndex\" md-border-bottom=\"\" md-dynamic-height=\"\" flex=\"\"><md-tab ng-repeat=\"task in vm.stream.tasks\" flex=\"\"><md-tab-label><span>{{ task.name }}</span></md-tab-label><md-tab-body><div layout=\"row\" layout-align=\"space-around center\"><div ng-hide=\"task.status == \'complete\'\" class=\"text-center\"><div ng-if=\"task.status == \'pending\'\" class=\"md-display-2\">Pending</div><div ng-if=\"task.status == \'running\'\"><div class=\"md-display-2\">{{ task.phase | executePhaseFilter }}</div><div><small>({{ task.plugin }})</small></div></div></div><div ng-if=\"task.status == \'complete\'\"><md-list><md-subheader class=\"md-no-sticky text-center\"><span>Accepted {{ task.accepted }}</span> <span>Rejected {{ task.rejected }}</span> <span>Accepted {{ task.failed }}</span> <span>Undecided {{ task.undecided }}</span></md-subheader><md-list-item class=\"md-2-line\" ng-repeat=\"entry in task.entries\"><md-icon class=\"fa fa-check-circle\"></md-icon><h4>{{ entry.title }}</h4><p><small>{{ entry.accepted_by }}{{ entry.rejected_by }}{{ entry.failed_by }}</small></p><md-icon class=\"md-secondary\" ng-click=\"doSecondaryAction($event)\" aria-label=\"Chat\" md-svg-icon=\"communication:message\"></md-icon></md-list-item></md-list><div flex=\"\">{{ entry.title }}</div></div></div></md-tab-body></md-tab></md-tabs><div layout=\"row\" layout-align=\"space-around center\"><div></div><md-button class=\"md-raised md-primary\" ng-click=\"vm.clear()\">Clear</md-button><div></div></div></div>");
$templateCache.put("plugins/movies/components/movie-entry/movie-entry.tmpl.html","<md-card class=\"movie-entry\"><div class=\"movie-poster\"><img ng-src=\"{{ ::vm.metadata.images.poster.medium }}\"></div><div class=\"movie-info\"><h3>{{ ::vm.movie.title }} ({{ ::vm.movie.year }}) <span class=\"rating\"><md-icon md-font-set=\"fa\" md-font-icon=\"fa-star\"></md-icon><span class=\"md-suhead\">{{ ::vm.metadata.rating | number:2 }}</span></span></h3><md-chips ng-model=\"::vm.metadata.genres\" readonly=\"true\"><md-chip-template>{{ $chip }}</md-chip-template></md-chips><p class=\"movie-plot\">{{ ::vm.metadata.overview }}</p></div><md-fab-speed-dial md-direction=\"left\" class=\"md-scale more-btn\"><md-fab-trigger><md-button aria-label=\"More\" class=\"md-fab md-mini\"><i class=\"fa fa-bars\" aria-hidden=\"true\"></i></md-button></md-fab-trigger><md-fab-actions><md-button aria-label=\"delete movie\" ng-click=\"vm.deleteMovie()\" class=\"md-fab md-raised md-mini\"><i class=\"fa fa-trash\" aria-hidden=\"true\"></i></md-button><md-button aria-label=\"More info\" class=\"md-fab md-raised md-mini\"><a target=\"_blank\" ng-href=\"http://www.imdb.com/title/{{ ::vm.metadata.imdb_id }}\"><i class=\"fa fa-film\" aria-hidden=\"true\"></i></a></md-button></md-fab-actions></md-fab-speed-dial></md-card>");
$templateCache.put("plugins/movies/components/new-list/new-list.tmpl.html","<md-dialog aria-label=\"Series Begin\" ng-cloak=\"\"><md-toolbar><div class=\"md-toolbar-tools\"><h2>New Movie List</h2><span flex=\"\"></span><md-button class=\"md-icon-button\" ng-click=\"vm.cancel()\"><md-icon md-font-icon=\"fa-times\" class=\"fa fa-lg\"></md-icon></md-button></div></md-toolbar><form name=\"newListForm\" ng-submit=\"vm.saveList()\"><md-dialog-content><div class=\"md-dialog-content\"><md-input-container><label>Name</label> <input type=\"text\" ng-model=\"vm.listName\" required=\"\"></md-input-container></div></md-dialog-content><md-dialog-actions><md-button ng-click=\"vm.cancel()\" class=\"md-default md-raised\">Cancel</md-button><md-button type=\"submit\" ng-disabled=\"newListForm.$invalid\" class=\"md-primary md-raised\">Save</md-button></md-dialog-actions></form></md-dialog>");
$templateCache.put("plugins/seen/components/seen-entry/seen-entry.tmpl.html","<md-card><md-card-header><md-card-header-text><span class=\"md-title\">{{vm.entry.title}}</span> <span class=\"md-subhead\" ng-if=\"vm.entry.local\">Local to <b>{{vm.entry.task}}</b></span> <span class=\"md-subhead\" ng-if=\"!vm.entry.local\">Global</span></md-card-header-text></md-card-header><md-card-content><md-list><md-list-item ng-repeat=\"field in ::vm.entry.fields\"><div class=\"md-list-item-text\" layout=\"row\"><p><b>{{field.field_name}}:</b> {{field.value}}</p></div></md-list-item></md-list></md-card-content><md-card-actions></md-card-actions></md-card>");
$templateCache.put("plugins/seen/components/seen-field/seen-field.tmpl.html","");
$templateCache.put("plugins/series/components/episode-releases/episode-releases.tmpl.html","<md-toolbar><div class=\"md-toolbar-tools\"><h2>Releases</h2><span flex=\"\"></span><md-button class=\"md-icon-button\" ng-click=\"vm.cancel()\"><md-icon md-font-icon=\"fa-times\" class=\"fa fa-lg\" aria-label=\"close dialog\"></md-icon></md-button></div></md-toolbar><md-dialog-content><div class=\"md-dialog-content\"><md-list flex=\"\"><md-list-item ng-repeat=\"release in vm.releases | orderBy : \'release_downloaded\' : true\" class=\"md-2-line episode-release\"><div class=\"md-list-item-text\"><h3 class=\"release-title\"><i ng-if=\"release.release_downloaded\" class=\"fa fa-download\"></i> {{ ::release.release_title }}</h3><p>{{ ::release.release_quality }}</p></div><md-button ng-click=\"vm.resetRelease(release)\" ng-if=\"release.release_downloaded\" class=\"md-icon-button\" aria-label=\"reset the release\"><i class=\"fa fa-refresh\" aria-hidden=\"true\"></i></md-button><md-button ng-click=\"vm.forgetRelease(release)\" class=\"md-icon-button\" aria-label=\"forget the release\"><i class=\"fa fa-trash\" aria-hidden=\"true\"></i></md-button></md-list-item></md-list></div></md-dialog-content>");
$templateCache.put("plugins/series/components/series-episode/series-episode.tmpl.html","<md-list-item layout=\"row\" layout-align=\"space-between\" class=\"series-episode\"><h3 flex=\"\">{{ ::vm.episode.episode_identifier }}</h3><md-button ng-disabled=\"vm.episode.episode_number_of_releases == 0\" ng-click=\"vm.showReleases()\">Releases</md-button><md-button ng-click=\"vm.deleteEpisode()\">Delete Episode</md-button><md-button ng-click=\"vm.deleteReleases()\">Delete Releases</md-button><md-button ng-click=\"vm.resetReleases()\">Reset Releases</md-button></md-list-item>");
$templateCache.put("plugins/series/components/series-show/series-show.tmpl.html","<md-card flex=\"\" class=\"series-entry\"><img ng-src=\"{{ ::vm.show.metadata.banner }}\" class=\"md-card-image\"><md-card-title flex=\"initial\"><md-card-title-text><span class=\"md-headline\">{{ ::vm.show.show_name }} <span class=\"rating\"><md-icon md-font-set=\"fa\" md-font-icon=\"fa-star\"></md-icon><span class=\"md-suhead\">{{ ::vm.show.metadata.rating }}</span></span></span><md-divider></md-divider><span class=\"md-subhead\">Latest: {{ ::(vm.show.latest_downloaded_episode.episode_identifier ? vm.show.latest_downloaded_episode.episode_identifier : \'No episode downloaded\') }}</span> <span class=\"md-subhead second-subhead\">Begin Episode: {{ (vm.show.begin_episode.episode_identifier ? vm.show.begin_episode.episode_identifier : \'No begin set\') }}</span><md-divider></md-divider><md-chips ng-model=\"vm.metadata.genres\" readonly=\"true\"><md-chip-template>{{ $chip }}</md-chip-template></md-chips></md-card-title-text></md-card-title><md-card-content flex=\"\" layout-gt-xs=\"row\" layout-xs=\"column\" class=\"custom-card\"><p>{{ ::vm.metadata.overview }}</p></md-card-content><md-fab-speed-dial md-direction=\"left\" class=\"md-scale more-btn\"><md-fab-trigger><md-button aria-label=\"More\" class=\"md-fab md-mini\"><i class=\"fa fa-bars\" aria-hidden=\"true\"></i></md-button></md-fab-trigger><md-fab-actions><md-button ng-click=\"vm.setBegin()\" aria-label=\"Set Series begin\" class=\"md-fab md-raised md-mini\"><i class=\"fa fa-play\" aria-hidden=\"true\"></i></md-button><md-button ng-click=\"vm.forgetShow()\" aria-label=\"forget show\" class=\"md-fab md-raised md-mini\"><i class=\"fa fa-trash-o\" aria-hidden=\"true\"></i></md-button><md-button ng-click=\"vm.alternateName()\" aria-label=\"alternate names\" class=\"md-fab md-raised md-mini\"><i class=\"fa fa-share-alt\" aria-hidden=\"true\"></i></md-button></md-fab-actions></md-fab-speed-dial><ng-transclude></ng-transclude></md-card>");
$templateCache.put("plugins/series/components/series-update/series-update.tmpl.html","<md-dialog aria-label=\"Series Begin\" ng-cloak=\"\"><md-dialog-content><form name=\"namesForm\"><div class=\"md-dialog-content\" ng-if=\"vm.params.alternate_names\" layout=\"column\" layout-padding=\"\"><h1 class=\"md-headline\">Series Alternate Names</h1><md-list><md-list-item ng-repeat=\"name in vm.params.alternate_names\"><span>{{ name }}</span></md-list-item></md-list></div></form><div class=\"md-dialog-content\" ng-if=\"!vm.params.alternate_names\"><h1 class=\"md-headline\">Series Begin</h1><md-input-container><label>Begin</label> <input type=\"text\" ng-model=\"vm.params.episode_identifier\"></md-input-container></div></md-dialog-content><md-dialog-actions><md-button ng-click=\"vm.cancel()\" class=\"md-primary\">Cancel</md-button><md-button ng-if=\"!vm.params.alternate_names\" ng-click=\"vm.save()\" class=\"md-warn\">Save</md-button></md-dialog-actions></md-dialog>");}]);