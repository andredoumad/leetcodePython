var twoSum = function(nums, target) {

    const dictionary = {};
    console.log(nums)
    for (let i = 0; i < nums.length; i++) {
      const findThis = target - nums[i];
      console.log('findThis ', findThis)
      console.log('dictionary ', dictionary)
      
      if (findThis in dictionary) {
          findThisIndex = nums.indexOf(findThis)
          console.log('findThisIndex ', findThisIndex)
          if (i != findThisIndex){
              const res = [];
              res.push(i)
              res.push(findThisIndex)
              
              res.sort()
              return res;
          }
      }
  
      dictionary[nums[i]] = i;
    }
  
    return null;

  };

console.log(twoSum([3, 5, 8, 2, 7, 11, 15], 9)) 

/*
[ 3, 5, 8, 2, 7, 11, 15 ]
findThis  6
dictionary  {}
findThis  4
dictionary  { '3': 0 }
findThis  1
dictionary  { '3': 0, '5': 1 }
findThis  7
dictionary  { '3': 0, '5': 1, '8': 2 }
findThis  2
dictionary  { '2': 3, '3': 0, '5': 1, '8': 2 }
findThisIndex  3
[ 3, 4 ]
*/