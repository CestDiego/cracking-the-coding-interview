////////////////////////////////////////

function LinkedList(){
  this.head = null;
}

function Node(value){
  this.value = value;
  this.next = null;
}

LinkedList.prototype.push = function(val){
  var node = new Node(val);
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

// 2.6 Adding numbers in linked lists

function addListNumbers(x, y, carry) {
  // Assuming X and Y are linked lists
  var resultNode = new Node(0),
      sum = carry;

  if (x === null && y === null && carry === 0) {
    return null
  }
  if (x !== null)
    sum += x.value
  if (y !== null)
    sum += y.value

  resultNode.value = sum % 10;

  if (x.next || y.next){
    var next_node = addListNumbers(x.next, y.next, sum > 10 ? 1 : 0)
    resultNode.next = next_node
  }
  else if (carry !== 0){
    var tmp = new Node(carry);
    resultNode.next = tmp;
  }

  return resultNode

};
