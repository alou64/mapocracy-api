"""empty message

Revision ID: 2be6f0018f02
Revises: 3c84ddc29760
Create Date: 2022-03-22 07:08:54.702674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2be6f0018f02'
down_revision = '3c84ddc29760'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('answer_poll_id_fkey', 'answer', type_='foreignkey')
    op.create_foreign_key(None, 'answer', 'poll', ['poll_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('email_list_user_id_fkey', 'email_list', type_='foreignkey')
    op.create_foreign_key(None, 'email_list', 'user', ['user_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('email_list_member_email_list_id_fkey', 'email_list_member', type_='foreignkey')
    op.drop_constraint('email_list_member_user_id_fkey', 'email_list_member', type_='foreignkey')
    op.create_foreign_key(None, 'email_list_member', 'user', ['user_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'email_list_member', 'email_list', ['email_list_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('poll_user_id_fkey', 'poll', type_='foreignkey')
    op.drop_constraint('poll_category_id_fkey', 'poll', type_='foreignkey')
    op.create_foreign_key(None, 'poll', 'user', ['user_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'poll', 'category', ['category_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('vote_poll_id_fkey', 'vote', type_='foreignkey')
    op.drop_constraint('vote_answer_id_fkey', 'vote', type_='foreignkey')
    op.drop_constraint('vote_user_id_fkey', 'vote', type_='foreignkey')
    op.create_foreign_key(None, 'vote', 'poll', ['poll_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'vote', 'answer', ['answer_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'vote', 'user', ['user_id'], ['id'], source_schema='public', referent_schema='public')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'vote', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'vote', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'vote', schema='public', type_='foreignkey')
    op.create_foreign_key('vote_user_id_fkey', 'vote', 'user', ['user_id'], ['id'])
    op.create_foreign_key('vote_answer_id_fkey', 'vote', 'answer', ['answer_id'], ['id'])
    op.create_foreign_key('vote_poll_id_fkey', 'vote', 'poll', ['poll_id'], ['id'])
    op.drop_constraint(None, 'poll', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'poll', schema='public', type_='foreignkey')
    op.create_foreign_key('poll_category_id_fkey', 'poll', 'category', ['category_id'], ['id'])
    op.create_foreign_key('poll_user_id_fkey', 'poll', 'user', ['user_id'], ['id'])
    op.drop_constraint(None, 'email_list_member', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'email_list_member', schema='public', type_='foreignkey')
    op.create_foreign_key('email_list_member_user_id_fkey', 'email_list_member', 'user', ['user_id'], ['id'])
    op.create_foreign_key('email_list_member_email_list_id_fkey', 'email_list_member', 'email_list', ['email_list_id'], ['id'])
    op.drop_constraint(None, 'email_list', schema='public', type_='foreignkey')
    op.create_foreign_key('email_list_user_id_fkey', 'email_list', 'user', ['user_id'], ['id'])
    op.drop_constraint(None, 'answer', schema='public', type_='foreignkey')
    op.create_foreign_key('answer_poll_id_fkey', 'answer', 'poll', ['poll_id'], ['id'])
    # ### end Alembic commands ###