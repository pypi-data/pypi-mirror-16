angular.module('opal.services').factory('TagService', function(Metadata) {
    "use strict";

    var TagService = function(existing_tags){

        var self = this;
        self.tags_list = [];
        self.currentFormTags = [];

        Metadata.then(function(metadata){
            self.tags_list = _.filter(_.values(metadata.tags), function(option){
                return option.direct_add;
            }).sort(function(x, y){ return y.name < x.name; });

            self.is_direct_add = function(someTag){
                return metadata.tags[someTag] && metadata.tags[someTag].direct_add;
            };

            self.currentFormTags = _.filter(existing_tags, function(t){
              return self.is_direct_add(t);
            });

            self.toSave = function(){
              var newTags = {};
              _.each(self.currentFormTags, function(t){
                newTags[t] = true;
              });

              // add back in the tags that are not direct add
              var not_direct_add = _.filter(existing_tags, function(t){
                  return !self.is_direct_add(t);
              });

              _.each(not_direct_add, function(t){
                newTags[t] = true;
              });

              return newTags;
            };
        });
    };

    return TagService;
});
