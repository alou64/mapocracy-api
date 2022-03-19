"""empty message

Revision ID: 66aab768c8e9
Revises: ea1d468c28f1
Create Date: 2022-03-19 10:14:22.850738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66aab768c8e9'
down_revision = 'ea1d468c28f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('answer_poll_id_fkey', 'answer', type_='foreignkey')
    op.create_foreign_key(None, 'answer', 'poll', ['poll_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('poll_user_id_fkey', 'poll', type_='foreignkey')
    op.drop_constraint('poll_category_id_fkey', 'poll', type_='foreignkey')
    op.create_foreign_key(None, 'poll', 'user', ['user_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'poll', 'category', ['category_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('vote_poll_id_fkey', 'vote', type_='foreignkey')
    op.drop_constraint('vote_user_id_fkey', 'vote', type_='foreignkey')
    op.drop_constraint('vote_answer_id_fkey', 'vote', type_='foreignkey')
    op.create_foreign_key(None, 'vote', 'user', ['user_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'vote', 'answer', ['answer_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'vote', 'poll', ['poll_id'], ['id'], source_schema='public', referent_schema='public')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'vote', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'vote', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'vote', schema='public', type_='foreignkey')
    op.create_foreign_key('vote_answer_id_fkey', 'vote', 'answer', ['answer_id'], ['id'])
    op.create_foreign_key('vote_user_id_fkey', 'vote', 'user', ['user_id'], ['id'])
    op.create_foreign_key('vote_poll_id_fkey', 'vote', 'poll', ['poll_id'], ['id'])
    op.drop_constraint(None, 'poll', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'poll', schema='public', type_='foreignkey')
    op.create_foreign_key('poll_category_id_fkey', 'poll', 'category', ['category_id'], ['id'])
    op.create_foreign_key('poll_user_id_fkey', 'poll', 'user', ['user_id'], ['id'])
    op.drop_constraint(None, 'answer', schema='public', type_='foreignkey')
    op.create_foreign_key('answer_poll_id_fkey', 'answer', 'poll', ['poll_id'], ['id'])
    # ### end Alembic commands ###