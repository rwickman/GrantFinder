# == Schema Information
#
# Table name: grants
#
#  id              :integer          not null, primary key
#  title           :string
#  release_date    :date
#  expired_date    :date
#  document_number :string
#  document_type   :string
#  activity_code   :string
#  clinical_trails :string
#  url             :string
#  created_at      :datetime         not null
#  updated_at      :datetime         not null
#

require 'test_helper'

class GrantTest < ActiveSupport::TestCase
  # test "the truth" do
  #   assert true
  # end
end
