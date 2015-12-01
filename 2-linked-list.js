////////////////////////////////////////

function LinkedList(){
  this.head = null;
}

LinkedList.prototype.push = function(val){
  var node = {
    value: val,
    next: null
  }
  if(!this.head){
    this.head = node;
  }
  else{
    current = this.head;
    while(current.next){
      current = current.next;
    }
    current.next = node;
  }
}

////////////////////////////////////////

function DoublyLinkedList(){
  this.head = null;
}

DoublyLinkedList.prototype.push = function(val){
  var head = this.head,
      current = head,
      previous = head;
  if(!head){
    this.head = {value: val, previous:null, next:null };
  }
  else{
    while(current && current.next){
      previous = current;
      current = current.next;
    }
    current.next = {value: val, previous:current, next:null}
  }
  return this
}


// swap a and b
// b = b - a
// a = b + a
// b = a - b

// Logical way
// a = a ^ b
// b = a ^ b
// a = a ^ b

function bubbleSort(arr){

  for(var i = arr.length - 1; i > 0; i--) {
    for(var j = 1; j <= i; j++) {
      if (arr[j-1] > arr[j]) {
        // swap
        var temp = arr[j-1];
        arr[j-1] = arr[j]
        arr[j]   = temp
      }
    }
  }
  return arr;
}

function selectionSort(arr) {
  for(var i = 0; i < arr.length - 1; i++) {
    var minIndex = i;
    for(var j = i + 1 ; j < arr.length; j++) {
      if (arr[j] < arr[i]) {
        minIndex = j
      }
    }
    if (minIndex !== i) {
      var temp = arr[i];
      arr[i]   = arr[minIndex];
      arr[minIndex]   = temp;
    }
  }
  return arr;
}
