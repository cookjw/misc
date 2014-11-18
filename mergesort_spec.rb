require_relative 'mergesort'

describe 'merge' do
  it 'should merge arrays correctly' do
    merge([5],[6]).should == [5,6]
    merge([7,8],[2,4]).should == [2,4,7,8]
    merge([1,3,5,6], [2,4,7,8]).should == [1,2,3,4,5,6,7,8]
    merge([1,2],[3]).should == [1,2,3]
    merge([6,7,8,9], [1,2,3,4,5]).should == [1,2,3,4,5,6,7,8,9]    
  end

end