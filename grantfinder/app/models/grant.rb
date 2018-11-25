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

class Grant < ApplicationRecord
    has_one :description,
        class_name: "GrantDescription",
        foreign_key: "grant_id",
        inverse_of: :grant,
        dependent: :destroy
    validates :url, uniqueness: true
end
